
class Model(torch.nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads)
 
    def forward(self, query, key, value):
        attn_weight = self.attn(query, key, value)[0]
        return attn_weight
# Initializing the model
m = Model(128, 16)

# Inputs to the model
x1 = torch.randn(4, 8, 32, 32)
x2 = torch.randn(256, 8, 16, 16)
