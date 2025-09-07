
class Model(torch.nn.Module):
    def __init__(self, config=None):
        super().__init__()
        self.query = torch.nn.Linear(config.hidden_size * 2, config.attention_head_size)
        self.key = torch.nn.Linear(config.hidden_size * 2, config.attention_head_size)
        self.value = torch.nn.Linear(config.hidden_size * 2, config.attention_head_size)
 
        # Weights for each head to get the attention output (shape: batch_size x hidden x num_heads x length)
        self.query_projection = torch.nn.Linear(config.attention_head_size, 1, bias=False)
 
    def forward(self, query, key, value, attn_mask):
        qk = self._compute_attention_scores(query, key) # shape: (batch x n_heads x len x len), where n_heads is equal to config.num_attention_head
        attn_weight = torch.softmax(qk, dim=-1)  # shape: (batch x n_heads x len x len)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # shape: (batch x n_heads x len x len)

        output = self._compute_attention_output(attn_weight, value, key, query)  # shape: (batch x n_heads x length x hidden_size * 2)
        return attn_weight, output
 
    def _compute_attention_scores(self, q, k):
        dqdk = self.query(q).unsqueeze(-1)  # shape: (batch x len x 1), where len is the length of query sequence
        dkdk = self.key(k).unsqueeze(-2)  # shape: (batch x 1 x len), where len is the length of key sequence
        dqdk, dkdk = torch.tanh(dqdk), torch.tanh(dkdk)  # shape: (batch x len x len)

        attn_score = torch.matmul(dqdk, dkdk.transpose(-2, -1)) / math.sqrt(self._head_dim)
        return attn_score
 
    def _compute_attention_output(self, attention_weights, value, k, q):
        # Shape: (batch x n_heads x length x hidden_size * 2), where n_heads is equal to config.num_attention_head
        dqdk = torch.matmul(attention_weights, self.value(value))  # shape: (batch x n_heads x length x hidden_size)
        dqdq = torch.einsum('bnhld,bnd->bndlh', [self.query_projection(k), q]) # Shape: (batch x n_heads x hidden_size x length)
        dqd1, dqd2, dqd3 = torch.split(dqdk + dqdq, self._head_dim, dim=-1)  # shape: (batch x n_heads x length x head_dim), where n_heads is equal to config.num_attention_head
        output = torch.cat([dqd2, dqd3], dim=-1)
        return output


# Initializing the model
m = Model(config=CONFIG)

# Inputs to the model
x = torch.randn(4, 8, 64, 64) # batch_size: 4; input_seq_length: 8; hidden_size: 32
query = x[:, :-1, :, :]  # shape: (batch_size x num_attention_head x query_length x hidden_dim), where num_attention_head is equal to CONFIG.num_attention_head and query_length is equal to input_seq_length - 1 (excluding the padding token)
key = x[:, :-1, :, :] # shape: (batch_size x num_attention_head x key_length x hidden_dim), where num_attention_head is equal to CONFIG.num_attention_head and query_length is equal to input_seq_length - 1 (excluding the padding token)
value = x[:, :-1, :, :] # shape: (batch_size x num_attention_head x key_length x hidden_dim), where num_attention_head is equal to CONFIG.num_attention_head and query_length is equal to input_seq_length - 1 (excluding the padding token)
attn_mask = torch.zeros(4, 8, 8, dtype=torch.float32) # shape: (batch x n_heads x len_q x len_k), where n_heads is equal to config.num_attention_head and query_length is equal to input_seq_length - 1 (excluding the padding token)
attn_mask[:, :, 0, 2] = 1 # set only the first three elements in attn_mask as 1, which are "The cat sat on the mat"
attn_mask[:, :, 0, 3] = 1
attn_weight, output = m(query, key, value, attn_mask)

