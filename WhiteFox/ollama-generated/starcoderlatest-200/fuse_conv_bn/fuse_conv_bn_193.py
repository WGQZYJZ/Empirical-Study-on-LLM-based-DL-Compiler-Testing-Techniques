
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        y = self.conv(x1)
        z = self.bn(y)
        return z


# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
