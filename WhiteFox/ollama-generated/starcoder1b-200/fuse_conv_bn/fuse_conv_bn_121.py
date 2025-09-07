
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn1  = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x):
        v = self.conv1(x)  # Fuse conv and bn into a single conv layer
        return self.bn1(v)


# Inputs to the model
x = torch.randn(1, 2, 2)
