
class ConvBN(torch.nn.Module):
    def __init__(self, num_channels, kernel_size=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_channels, num_channels, kernel_size)
        self.bn  = torch.nn.BatchNorm2d(num_channels, eps=1e-5, momentum=0.01)

    def forward(self, x):
        output = self.conv(x)
        output = self.bn(output)
        return output


# Initializing the model
m = ConvBN(3)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
