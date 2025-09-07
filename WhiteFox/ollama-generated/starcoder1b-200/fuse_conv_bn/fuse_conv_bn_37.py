
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(...)
        self.bn     = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        x1 = self.conv1(x1)
        x1 = self.bn(x1)
        return x1


# Inputs to the model
x1  = torch.randn(1, 3, 48, 48)
