
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
 
    def forward(self, query, key, value):
        v  = self.attention(query, key, value)[0] # (batch_size, src_len, embed_dim)
        return v


# Initializing the model
m = Model()
# Inputs to the model
q = torch.randn(4, 128, 5, embed_dim=embed_dim)
k = torch.randn(4, 128, 3, embed_dim=embed_dim)
v = torch.randn(4, 128, 6, embed_dim=embed_dim)
