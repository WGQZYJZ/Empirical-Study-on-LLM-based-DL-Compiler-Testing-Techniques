
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 1)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        conv_output = self.conv(x)
        return self.bn(conv_output)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
