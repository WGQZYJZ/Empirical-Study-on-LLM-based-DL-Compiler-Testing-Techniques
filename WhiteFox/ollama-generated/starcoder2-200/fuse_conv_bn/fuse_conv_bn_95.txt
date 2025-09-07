
class ConvBn(nn.Module):
    def __init__(self, in_channels: int = 32, out_channels: int = 64) -> None:
        super().__init__()

        self._conv_layer = nn.Conv2d(in_channels=in_channels,
                                      out_channels=out_channels, kernel_size=10, stride=5)
        
        self._bn = nn.BatchNorm2d(num_features=64)

    def forward(self, x):
        v  = self._conv_layer(x)
        v2 = self._bn(v)

        return v2

model = ConvBn()

