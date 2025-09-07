
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, hidden_size, num_heads):
        super().__init__()

        self.hidden_size = hidden_size # the dimension of the input and output
        self.num_heads = num_heads   # number of heads

    # Note that in general, we need to compute:
    #     key: [batch x len(key) x seq_len x hid_dim]
    #     value: [batch x len(value) x seq_len x hid_dim]
    def forward(self, query, key, value):
        batch_size = query.shape[0]

        # [seq_len x batch x num_heads x head_dim]
        q = query.view(-1, self.hidden_size).transpose(0, 1)   # (batch, seq_len, hidden_size) => (seq_len, batch, hidden_size)
        k = key.view(-1, self.hidden_size).transpose(0, 1)     # (batch, seq_len, hidden_size) => (seq_len, batch, hidden_size)
        v = value.view(-1, self.hidden_size).transpose(0, 1)   # (batch, seq_len, hidden_size) => (seq_len, batch, hidden_size)
        
        qk = torch.matmul(q, k)                                # (seq_len, batch, num_heads, head_dim)
        softmax_qk = qk / math.sqrt(self.hidden_size)      # (seq_len, batch, num_heads, head_dim)
        
        output = self._scaled_dot_product_attention(softmax_qk, v)  # (seq_len, batch, hid_dim)
        output = output.transpose(0, 1).contiguous().view(batch_size, -1, self.hidden_size)    # (batch, seq_len, hidden_size) => (batch, seq_len * hid_dim)

        return output
 
    # Scaled Dot Product Attention
    def _scaled_dot_product_attention(self, qk, v):
        batch_size = qk.shape[0]
        
        attn = torch.matmul(qk, v.transpose(-2, -1))    # (seq_len, batch, num_heads, head_dim) => (seq_len, batch, head_dim, num_heads)
        scaled_attn = attn / math.sqrt(self.hidden_size) # (seq_len, batch, head_dim, num_heads)
        
        output = torch.matmul(scaled_attn, self._o2.transpose(-1, -2))  # (seq_len, batch, hid_dim) => (batch, seq_len, hid_dim)
        return output

    def initialize_parameters(self):
        self._o2 = torch.nn.Parameter(torch.zeros((self.hidden_size, self.num_heads * self.hidden_size))) # initialize parameter


# Initializing the model
m = MultiHeadSelfAttention(1024, 8)

# Inputs to the model
query = torch.randn(3, 64, 1024)
key = torch.randn(3, 64, 1024)
value = torch.randn(3, 64, 1024)
