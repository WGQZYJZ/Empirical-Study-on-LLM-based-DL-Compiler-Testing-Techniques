
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 6, 6)
