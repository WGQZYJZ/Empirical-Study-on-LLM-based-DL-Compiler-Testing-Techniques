
class Model(torch.nn.Module):
    def __init__(self, input_channels):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        conv = self.conv(x1) # fuse
        bn = self.bn(conv) # fuse
        return bn
