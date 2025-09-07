
class ConvBn(torch.nn.Module):
    def __init__(self, channel):
        super().__init__()

        self.conv = torch.nn.Conv2d(channel, 10, kernel_size=3)
        self.bn = torch.nn.BatchNorm2d(10)

    def forward(self, x):
        return self.bn(torch.nn.functional.conv2d(x, self.conv.weight))

# Initializing the model
m = ConvBn(channel=3)

 # Input to the model
    input_tensor = torch.randn(1000000, 3, 8, 4)

    # Inputs to the model
    x = torch.randn(500, 200, 6)

# Initializing the model
m = Model()

