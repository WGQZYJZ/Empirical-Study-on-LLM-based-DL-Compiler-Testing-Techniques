
class ConvBN(torch.jit.script):
    def __init__(self, conv, bn):
        super().__init__()
        self.conv  = conv
        self.bn    = bn
        self.weight_buffer  = None
        self.bias_buffer   = None

    def forward(self, x):
        weight = getattr(self, "weight", None)
        if weight is not None:
            weight = FuseConvBN().fuse_conv_bn(x, weight)
        return F.linear(x, conv, bias=bn)

# Initializing the model
c1 = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
b1 = torch.nn.BatchNormXd(...) # X should match with ConvXd
m1 = ConvBN(c1, b1)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
