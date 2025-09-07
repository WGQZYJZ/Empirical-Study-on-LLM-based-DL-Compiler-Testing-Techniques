
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x1):
        v = self.conv(x1)
        bn = self.bn(v)
        return bn

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
