
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.conv3d(x1, self.linear1, bias=None) # this pattern is not supported by fuse_conv_bn
        v3  = torch.nn.functional.batchnorm2d(v2)

# Initializing the model
m = Model()


# Inputs to the model