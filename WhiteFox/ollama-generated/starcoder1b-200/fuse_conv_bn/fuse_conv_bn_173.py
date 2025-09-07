
class Model(torch.nn.Module):
    def __init__(self, conv=None, bn=None):
        super().__init__()
        if not isinstance(conv, torch.nn.ConvXd) and not isinstance(bn, torch.nn.BatchNormXd):
            raise ValueError('The convolution layer should be implemented in module')

        self.conv  = conv
        self.bn    = bn

    def forward(self, x1):
        x2 = self.conv(x1) # X can be 1, 2, or 3 representing the dimension
        return self.bn(x2)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
