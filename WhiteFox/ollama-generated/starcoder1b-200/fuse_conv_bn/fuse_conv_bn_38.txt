
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X should be a channel first convolution layer
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        return self.bn(self.conv(x1))

