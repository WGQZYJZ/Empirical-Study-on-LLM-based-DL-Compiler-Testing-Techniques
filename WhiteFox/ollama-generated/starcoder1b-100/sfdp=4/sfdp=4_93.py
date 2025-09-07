
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        w1 = self.conv(x1)
        v1 = w1 * 0.5
        v2 = w1 * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v2 + 1
        w3 = self.conv(x2)
        v5 = w3 * 0.5
        v6 = w3 * 0.7071067811865476
        v7 = torch.erf(v6)
        w4 = self.conv(x1, x2)
        v8 = w4 * 0.5
        v9 = w4 * 0.7071067811865476
        v10 = torch.erf(v9)
 
        return v1 + v3 + v5 + v8 + v10

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
