
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...)  # X should match with Conv2d
        self.linear = ...

    def forward(self, x):
        out_conv = self.conv(x)  # Use the output of the convolution layer as the input to a batch norm layer
        bn      = self.bn(out_conv)  # This line is not needed for the functional API equivalent above
        return self.linear(bn)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(...)  # X should be 1, 2, or 3 representing the dimension
