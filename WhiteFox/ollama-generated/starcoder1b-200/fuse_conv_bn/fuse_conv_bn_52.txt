
class Model(torch.nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        return self.bn(self.conv(x1))


# Inputs to the model
in_channels = 1
