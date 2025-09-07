
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.ConvXd(20)
        bn  = torch.nn.BatchNorm2d(conv)
        bn  = torch.nn.BatchNormXd(bn) # bn is actually used to check the batch norm. It shouldn't be a problem because it has already been removed by fuse_conv_bn.
        return conv(x1, )


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(20) # A random 1D tensor with size [20] is created as input.
__output__  = m(x1)
