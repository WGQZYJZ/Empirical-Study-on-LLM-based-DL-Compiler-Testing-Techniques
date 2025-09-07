
class Model(torch.nn.Module):
    def __init__(self, num_features=3, kernel_size=2, stride=2, padding=0, groups=1):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x):
        output = self.bn(self.conv(x))
        return output

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 4, 4)
