
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 16, 3, stride=2)
        self.bn = torch.nn.BatchNorm2d(16)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 1, 48, 64)
