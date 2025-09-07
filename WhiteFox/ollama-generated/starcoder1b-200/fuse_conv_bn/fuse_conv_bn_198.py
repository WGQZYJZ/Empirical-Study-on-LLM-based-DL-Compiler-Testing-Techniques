
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 2, or 3 representing the dimension
        self.bn  = torch.nn.BatchNorm2d(...) # X should match with ConvXd

    def forward(self, x1):
        return self.bn(self.conv(x1))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 256, 256)
