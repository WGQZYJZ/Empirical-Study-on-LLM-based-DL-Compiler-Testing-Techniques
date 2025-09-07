
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, kernel_size=3, padding=1)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.bn(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(3, 1, 5, 5)
