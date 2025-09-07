
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.ConvXd(**kwargs)
        self.bn = torch.nn.BatchNormXd()

    def forward(self, x):
        output = self.bn(self.conv(x)) # fuse batchnorm with conv2d
        return output


# Initializing the model
m = Model(16, 3, 3)

# Inputs to the model
x = torch.randn(20, 4, 8, 8)
