
class Model(torch.nn.Module):
    def __init__(self, conv, bn):
        super().__init__()
        self.conv = conv

    def forward(self, x1):
        return self.conv(x1)


class ConvBnBlock(torch.nn.Module):
    def __init__(self, input_channels, output_channels, kernel_size, stride, padding, dilation=1, groups=1):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension of the convolution layer
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.bn(v1)
        return v2


class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        ...  # Register conv and bn as nn.modules or torch.functional equivalents for their functional API equivalent

    def forward(self, x):
        ...
        return v1  # Output of the first block should be used by second and third blocks
# Initialization and generating input tensors
conv = ...
bn = ...
net = Net()
