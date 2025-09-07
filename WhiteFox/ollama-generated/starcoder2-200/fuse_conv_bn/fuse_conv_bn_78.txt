
class ConvBnModel(torch.nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        self.conv = torch.nn.Conv1d(in_channels=32, out_channels=64)

    def forward(self, x):
      self.conv  = nn.fuse_conv_bn(self.conv, self.norm)
      return self.conv(x)


# Initializing the model
m = ConvBnModel()

