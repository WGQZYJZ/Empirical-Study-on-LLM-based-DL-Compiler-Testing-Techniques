
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim, num_heads)
 
    def forward(self, x1, key, query, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk.matmul(value)
        return attention, output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, embed_dim, seq_len, embed_dim)
key = torch.randn(embed_dim, embed_dim, num_heads, query_len)
query = torch.randn(embed_dim, embed_dim, num_heads, key_len)
value = torch.randn(embed_dim, embed_dim, num_heads, value_len)
__output__, __intermediate_output__ = m(x1, key, query, value)

