
class Model(torch.nn.Module):
    def __init__(self, num_channels):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=num_channels, out_channels=32, kernel_size=4)
        self.bn = torch.nn.BatchNorm2d(num_features=32, eps=1e-05, momentum=0.1, affine=True)

    def forward(self, x):
        output = self.conv(x)  # This should be replaced by ConvXd
        output = self.bn(output)  # This should be replaced by BatchNormXd

# Initializing the model
m = Model(num_channels=3)


# Inputs to the model
x1 = torch.randn(2, 3, 4, 5)
