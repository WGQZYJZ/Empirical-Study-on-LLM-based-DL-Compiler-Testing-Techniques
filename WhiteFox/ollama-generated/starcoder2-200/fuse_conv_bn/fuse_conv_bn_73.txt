
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.Conv2d(x1)
        bn  = torch.nn.BatchNorm2d()

        conv_bn = torch.ops.quantized.fuse_conv_bn(conv, bn).float().to(conv)
        return conv_bn


# Initializing the model
m  = Model()

# Input tensor to the model
x1 = torch.randn(1024, 3, 32, 32)
__output__  = m(x1)

