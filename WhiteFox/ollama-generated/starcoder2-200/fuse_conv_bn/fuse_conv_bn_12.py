
class MyModel(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()

        # conv: 3x3 convolution with 16 channels, stride=2 and no padding on both sides of the kernel
        self.conv = nn.Conv2d(in_channels, out_channels, 3, 2)

