
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim, num_heads)
 
    def forward(self, q1, k1, v1):
        output = self.attention(q1, k1, v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(batch_size, num_heads, len_query, embed_dim)
k1 = torch.randn(batch_size, num_heads, len_key, embed_dim)
v1 = torch.randn(batch_size, num_heads, len_value, embed_dim)
