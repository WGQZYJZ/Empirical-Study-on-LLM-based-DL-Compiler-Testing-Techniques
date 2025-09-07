
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        y = self.conv(x)
        z = self.bn(y)
        return z


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 1, 2)
