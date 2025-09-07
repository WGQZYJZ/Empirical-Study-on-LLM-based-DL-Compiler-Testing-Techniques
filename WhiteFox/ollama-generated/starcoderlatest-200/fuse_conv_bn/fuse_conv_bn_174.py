
class Model(torch.nn.Module):
    def __init__(self, input_channels):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(input_channels, 32, kernel_size=5)
        self.bn1 = torch.nn.BatchNorm2d(32)
        # ...

    def forward(self, x):
        # ...
        return output
# Initializing the model
m = Model(3)


# Inputs to the model
x1 = torch.randn(2, 3, 5, 6)
