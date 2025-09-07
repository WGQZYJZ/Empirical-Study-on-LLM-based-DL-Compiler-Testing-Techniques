
class UpsampleConv2d(torch.nn.Module):
    def __init__(self, kernel_size, stride=1, padding=0):
        super().__init__()
        self.upsample = nn.Upsample(scale_factor=2, mode='bilinear', align_corners=True)
        self.conv = torch.nn.Conv2d(in_channels=kernel_size ** 2, out_channels=1, kernel_size=kernel_size, stride=stride, padding=padding, bias=False)
 
    def forward(self, x):
        return self.upsample(self.conv(x))


# Initializing the model
m = UpsampleConv2d(kernel_size=3, stride=1, padding=1)


