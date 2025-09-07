
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X should be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)  # X should match with ConvXd
        self.linear = torch.nn.Linear(...)

    def forward(self, x):
        output = self.bn(self.conv(x))
        return self.linear(output)


# Initializing the model
m = Model()


