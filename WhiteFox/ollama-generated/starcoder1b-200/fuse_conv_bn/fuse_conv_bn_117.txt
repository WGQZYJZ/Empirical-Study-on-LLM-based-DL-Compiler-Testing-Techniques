
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.linear = torch.nn.Linear(self.conv.out_channels, 2)

    def forward(self, x):
        return self.bn(self.conv(x))


# Inputs to the model
x1 = torch.randn(1, 3, 3, 3)
