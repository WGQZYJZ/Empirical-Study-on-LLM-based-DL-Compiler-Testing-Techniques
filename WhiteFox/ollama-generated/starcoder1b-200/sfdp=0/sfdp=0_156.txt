
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        v3 = v1 * 0.5
        v4 = v2 * 0.7071067811865476
        v5 = torch.erf(v3)
        v6 = v4 + 1
        v7 = (v6 * x1).sum(-1, keepdim=True) + (x2.abs().pow(2)).sum(0, keepdim=True) ** -0.5
        v8 = v5 * v7
        return v8


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
