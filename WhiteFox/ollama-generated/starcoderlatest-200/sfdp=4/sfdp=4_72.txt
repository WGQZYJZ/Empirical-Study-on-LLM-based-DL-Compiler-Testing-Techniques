
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, q1, k1, v1, attn_mask=None):
        d1, h1 = self.attention(q1, k1, v1, attn_mask)
        return d1

# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(2, 3, 64, 64)
k1 = torch.randn(2, 3, 64, 64)
v1 = torch.randn(2, 8, 64, 64)
attn_mask = torch.ones((2, 1, 64, 64), dtype=torch.float32)
