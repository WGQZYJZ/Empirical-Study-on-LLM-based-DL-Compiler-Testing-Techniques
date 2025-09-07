
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2)
        v2 = t1 * 0.5 + t2 * 0.7071067811865476 + t3 * 0.9223372036854776
        v3 = torch.erf(v2)
        v4 = v2 * v3
        v5 = v1 + v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
