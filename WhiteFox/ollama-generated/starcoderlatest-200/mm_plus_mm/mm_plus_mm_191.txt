
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv(x1) * 0.5
        v2 = self.conv(x2) * 0.7071067811865476
        v3 = torch.erf(self.conv(x3))
        v4 = torch.erf(self.conv(x4))
        v5 = v3 + v4
        v6 = self.conv(v5) * 0.5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
x3 = torch.randn(1, 8, 64, 64)
x4 = torch.randn(1, 8, 64, 64)
