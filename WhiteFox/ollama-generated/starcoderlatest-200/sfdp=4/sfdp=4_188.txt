
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = Attention()
 
    def forward(self, query, key, value, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


class Attention(torch.nn.Module):
    def __init__(self, query_size, key_size, value_size, head=8):
        super().__init__()
 
        self.query = torch.nn.Linear(query_size, head * 3)  # Apply a linear transformation to the queries (and keys and values).
        self.key = torch.nn.Linear(key_size, head * 3)
        self.value = torch.nn.Linear(value_size, head * 3)
 
        self.linear_out = torch.nn.Linear(head * 3, query_size)  # Apply a linear transformation to the output of the attention layer (as well as to the intermediate variables)
 
    def forward(self, x):
        batch_size, seq_len, d_model = x.shape
 
        # Project each input tensor into the same dimensionality for easy access.
        queries = self.query(x).view(batch_size, seq_len, 3, -1).permute(0, 2, 1, 3)  # (B, head, QK dim, d_model / QK dim)
        keys = self.key(x).view(batch_size, seq_len, 3, -1)
        values = self.value(x).view(batch_size, seq_len, 3, -1)
 
        # Apply the attention mechanism to the queries and keys (performing the dot product between each query and key), then scale it by square root of dimensionality. This results in QK matrix with shape: (B, head, SeqLen, SeqLen).
        qk = queries @ keys.transpose(-2, -1) / math.sqrt(queries.size(-1))
 
        # Combine the heads to produce a context vector. This is achieved by using the output of each head as the input into the linear transformation and summing them. Shape (B, head * dim).
        attn_context = qk.permute(0, 2, 1, 3).contiguous().view(batch_size, -1, seq_len)
 
        # Combine the heads to produce a context vector. This is achieved by using the output of each head as the input into the linear transformation and summing them. Shape (B, head * dim).
        attn_context = attn_context @ self.linear_out(attn_context)
 
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 200, 384)
