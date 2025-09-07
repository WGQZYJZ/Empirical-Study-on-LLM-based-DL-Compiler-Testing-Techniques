
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = t1[:, :size] * 0.5
        v3 = t1[:, :size] * 0.7071067811865476
        v4 = torch.erf(v3) + 1
        v5 = v2 * v5
        return v5


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 9, 9)
