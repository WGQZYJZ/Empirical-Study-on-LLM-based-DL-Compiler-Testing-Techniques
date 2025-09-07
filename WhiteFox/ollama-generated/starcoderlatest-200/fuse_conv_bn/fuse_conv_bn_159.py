
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7)
        self.bn    = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        x1 = self.conv1(x1)
        return self.bn(x1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 56, 56)
