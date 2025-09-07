
class Model(torch.nn.Module):
    def __init__(self, inp=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3=None):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        if x3 is None:
            v4 = torch.erf(v3)
            v5 = v4 + 1
        else:
            v4 = self.conv(x2, x3)
            v5 = torch.matmul(v4, v3)
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
inp  = torch.randn(1, 10, 3, 3)
x1   = torch.randn(4, 1, 28, 28)
x2   = x1 + inp
