
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(0.5)
        v2 = v1 * v1
        v3 = v2 * v1
        v4 = torch.exp(v3).pow(0.044715)
        v5 = (v4 + 1) * 0.7978845608028654
        v6 = v5 * 0.7071067811865476
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
