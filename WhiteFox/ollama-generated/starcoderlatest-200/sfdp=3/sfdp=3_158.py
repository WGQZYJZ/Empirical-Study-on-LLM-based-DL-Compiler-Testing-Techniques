
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=10, num_heads=8)
 
    def forward(self, qk, x2):
        v  = self.attention(qk, x2)[0] # Retrieve the output of multi-head attention
        return v
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2 = torch.randn(8, 10, 64, 64)
