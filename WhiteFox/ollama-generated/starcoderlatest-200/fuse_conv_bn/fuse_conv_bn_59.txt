
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, (2, 2), (1, 2))
        self.bn = torch.nn.BatchNorm2d(6)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x


# Initializing the model
m = Model()
m.eval()

# Inputs to the model
x1 = torch.randn(2, 1, 5, 5)
