
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=8, qkv_same_shape=True)
 
    def forward(self, x1, x2):
        v1, v2 = self.attn(x1, x2)
        return v1
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
