
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        return v2


# Initializing the model
m = Model()


