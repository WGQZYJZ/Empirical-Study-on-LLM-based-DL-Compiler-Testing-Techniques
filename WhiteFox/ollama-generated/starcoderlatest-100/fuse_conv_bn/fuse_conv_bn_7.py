
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x1):
        output = self.conv(x1)
        return self.bn(output)


# Inputs to the model
x1 = torch.randn(1, 1, 3, 3)
