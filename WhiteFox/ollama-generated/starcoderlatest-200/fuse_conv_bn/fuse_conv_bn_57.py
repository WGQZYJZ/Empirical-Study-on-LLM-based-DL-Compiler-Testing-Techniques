
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, kernel_size=(4, 4), padding=((0, 0), (1, 1)), stride=(1, 1))
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        return self.bn(self.conv(x))


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 1, 4, 4)
