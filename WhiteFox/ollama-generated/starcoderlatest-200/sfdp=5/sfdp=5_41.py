
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_1 = torch.nn.MultiheadAttention(3, 8)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, q1, k1):
        v1 = self.attn_1(q1, k1, v1)[0]
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
q1 = torch.randn(8, 3, 64, 64)
k1 = torch.randn(8, 3, 64, 64)
