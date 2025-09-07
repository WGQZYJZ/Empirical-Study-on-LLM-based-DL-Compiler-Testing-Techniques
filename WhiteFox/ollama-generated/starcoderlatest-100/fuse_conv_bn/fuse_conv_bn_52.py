
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        conv_output = self.conv(x)
        bn_output   = self.bn(conv_output)
        return bn_output


# Inputs to the model
x = torch.randn(1, 3, 6, 4)
