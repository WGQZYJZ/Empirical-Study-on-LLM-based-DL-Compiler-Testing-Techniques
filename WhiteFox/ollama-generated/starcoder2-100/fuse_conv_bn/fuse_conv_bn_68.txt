
class ConvModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 40, 5)
        bn   = torch.nn.BatchNorm2d(40)
        output = bn(conv(x1)) # fuse_conv_bn() should be triggered here
        return output

m = ConvModel()
input_tensor = torch.randn(16, 3, 128, 128)
__output__   = m(input_tensor)

