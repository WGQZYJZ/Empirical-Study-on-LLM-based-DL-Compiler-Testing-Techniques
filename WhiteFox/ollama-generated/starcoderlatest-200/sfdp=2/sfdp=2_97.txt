
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, x1, x2, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(8)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(16, 8, 64, 64) # The query in MultiheadAttention has shape (num_heads, head_dim, batch_size, seq_len)
key  = torch.randn(32, 8, 64, 64) # The key in MultiheadAttention has shape (num_heads, head_dim, batch_size, seq_len)
value  = torch.randn(16, 8, 64, 64) # The value in MultiheadAttention has shape (num_heads, head_dim, batch_size, seq_len)


# Outputs of the model
