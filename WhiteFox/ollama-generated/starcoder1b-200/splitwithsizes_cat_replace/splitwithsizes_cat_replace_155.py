
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(v1)
        v3 = v2 * 0.5
        v4 = v2 * 0.7071067811865476
        v5 = torch.erf(v3)
        v6 = v4 + 1
        v7 = v6 * x2
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1, x2 = torch.randn(2, 3, 64, 64), torch.randn(1, 8)
