
class Model(torch.nn.Module):
    def __init__(self, channels, kernel_size, stride=1):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        return v2


# Initializing the model
m = Model(..., channels=3, kernel_size=(3, 4, 5))
m.eval() # The BN layer is set in evaluation mode
m.fuse_conv_bn(m.conv, m.bn) # Set to evaluation and fuse conv and bn layers
