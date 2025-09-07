
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, kernel_size=(3, 3))
        self.bn = torch.nn.BatchNorm2d(32)

    def forward(self, x):
        output = self.bn(F.relu(self.conv(x)))
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 1, 56, 56)
