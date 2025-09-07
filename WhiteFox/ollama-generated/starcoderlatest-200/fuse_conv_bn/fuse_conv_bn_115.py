
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        v1 = self.conv(x1)
        bn_output = self.bn(v1)
        return bn_output


# Inputs to the model
x1 = torch.randn(1, 1, 5, 5)
