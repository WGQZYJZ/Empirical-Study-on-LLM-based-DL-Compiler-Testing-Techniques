
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, kernel_size=(2, 2))
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        output = self.bn(self.conv(x))
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
