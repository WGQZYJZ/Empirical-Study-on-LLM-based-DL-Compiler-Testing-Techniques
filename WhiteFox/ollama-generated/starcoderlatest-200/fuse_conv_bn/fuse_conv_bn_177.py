
class Model(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=in_channels,
                                    out_channels=out_channels,
                                    kernel_size=(1, 3),
                                    stride=(1, 2))
        self.bn = torch.nn.BatchNorm2d(out_channels)

    def forward(self, x):
        output = F.relu(self.conv(x), inplace=False) # The parameter 'inplace' is added to allow the use of this pattern without specifying this argument explicitly in all functions where it is used. In general, this value should always be set to False.
        return self.bn(output)


# Initializing the model
m = Model(2, 3) # The input tensor shape is [1, 2, 4] as shown above.

# Inputs to the model
x = torch.randn(1, 2, 4)
