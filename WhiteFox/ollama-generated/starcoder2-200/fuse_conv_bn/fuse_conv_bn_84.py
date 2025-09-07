
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1: torch.Tensor) -> torch.Tensor: # this line is for testing. Do not modify it!
        conv = torch.nn.Conv2d(32, 64, 5)
        bn  = torch.nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True)
        conv_output  = conv(input1)
        bn_output    = bn(conv_output) # fuse_conv_bn will replace it with a new layer
        return bn_output

# Initializing the model
m = Model()


# Input to the model
x1 = torch.randn(8, 32, 64, 50)


