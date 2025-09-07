
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 1, 1)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        output = self.conv(x1)
        output = self.bn(output)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 5, 5)
