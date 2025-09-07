
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if inp is None:
            self.inp = torch.randn(1, 3, 64, 64)
        else:
            self.inp = inp
 
    def forward(self, x1, inp=None):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + inp
        v6 = v2 * v5
        return v6


# Inputs to the model
inp = torch.randn(1, 3, 64, 64)
