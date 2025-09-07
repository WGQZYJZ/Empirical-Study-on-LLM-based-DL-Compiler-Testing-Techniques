
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x1):
        output = self.conv(input_tensor)
        return self.bn(output)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
