
class Model(torch.nn.Module):
    def __init__(self, input_channel=1024):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_channel, 64, kernel_size=(3, 3))

    def forward(self, x1):
        bn1 = torch.nn.BatchNorm2d(x1)
        return bn1(self.conv(x1))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1024, 3, 3)
