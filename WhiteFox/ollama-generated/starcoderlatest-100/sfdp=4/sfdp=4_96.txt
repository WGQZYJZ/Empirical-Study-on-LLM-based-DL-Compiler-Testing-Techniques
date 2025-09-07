
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=8, num_heads=1)
 
    def forward(self, query, key, value, attn_mask):
        v, _ = self.attention(query, key, value, attn_mask)
        return v


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, 8, 64, 64)
k1 = torch.randn(1, 8, 64, 64)
v1 = torch.randn(1, 8, 64, 64)
attn_mask  = (q1 > q2).byte() * -1e3 # Generate an attention mask with random values
