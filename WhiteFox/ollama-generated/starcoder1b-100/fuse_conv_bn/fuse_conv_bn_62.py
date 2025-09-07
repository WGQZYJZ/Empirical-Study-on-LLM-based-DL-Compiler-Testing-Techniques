
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)
        self.bn   = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.bn(v1)  # X should match with ConvXd
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
