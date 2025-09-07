
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp=None):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        if inp is not None:
            v5 = v4 + inp
        else:
            v5 = v4
        return v2 * v5


# Initializing the model
m = Model()
inp = 0
x1 = torch.randn(1, 3, 64, 64)
