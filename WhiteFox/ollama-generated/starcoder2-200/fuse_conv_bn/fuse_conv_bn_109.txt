
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.Conv1d(256, 397)
        bn  = torch.nn.BatchNorm2d(397)
        output  = bn(conv(x1)) # fuse_conv_bn
        return output


m = Model()
x1 = torch.randn(408, 256, 149)
__output__  = m(x1)

# Inputs to the model: 
x1 = torch.randn(3, 256, 149)

