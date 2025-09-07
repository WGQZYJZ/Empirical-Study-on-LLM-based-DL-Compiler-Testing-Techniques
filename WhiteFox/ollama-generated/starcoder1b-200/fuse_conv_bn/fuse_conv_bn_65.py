
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 3 or 4 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        return self.bn(self.conv(x))


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 28, 28)
