
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x):
        y = self.conv(x)
        z = self.bn(y)
        return z


# Inputs to the model
x = torch.randn(1, 2, 2)
