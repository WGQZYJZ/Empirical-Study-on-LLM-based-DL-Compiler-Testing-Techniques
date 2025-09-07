
class Model(torch.nn.Module):
    def __init__(self, kernel_size=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, kernel_size)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        return self.bn(self.conv(x))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(100, 3, 548, 597).to('cuda')
