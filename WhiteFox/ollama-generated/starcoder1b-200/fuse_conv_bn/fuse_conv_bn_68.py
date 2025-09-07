
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        x = self.conv(x1)
        return self.bn(x)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
