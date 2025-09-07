
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.relu = torch.nn.LeakyReLU()

    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = self.conv(x1) * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        v4 = torch.where(v2 > 0, x1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
