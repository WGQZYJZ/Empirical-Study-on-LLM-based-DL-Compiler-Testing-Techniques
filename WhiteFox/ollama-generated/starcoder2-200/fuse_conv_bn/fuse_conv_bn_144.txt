
class ConvBN(torch.nn.Module):
    def __init__(self, in_, out_, kernel=3, padding=0, stride=1):
        super().__init__()

        self.conv  = torch.nn.Conv2d(in_, out_, kernel, padding=padding, stride=stride)
        self.bn = torch.nn.BatchNorm2d(out_)

    def forward(self, x):
        y  = conv_bn(x)

m  = ConvBN(3, 4).eval()

# Inputs to the model
x1 = torch.randn(8, 3, 700, 562)

