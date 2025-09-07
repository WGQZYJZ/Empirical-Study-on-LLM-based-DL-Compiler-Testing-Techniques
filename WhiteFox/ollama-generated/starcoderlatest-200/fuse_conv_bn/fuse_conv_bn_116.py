 
class ConvNet(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        y = self.conv(x)
        z = self.bn(y)
        return z


# Initializing the model
m  = ConvNet()

# Inputs to the model
input_tensor = torch.randn(100, 3, 28, 28)
__output__  = m(x)


