
class Model(torch.nn.Module):
    def __init__(self, conv1d):
        super().__init__()
        self.conv1d = conv1d

    def forward(self, x1):
        v1 = self.conv1d(x1)
        return v1


# Initializing the model and specifying the ConvXd pattern 
m = Model(torch.nn.Conv2d(in_channels=10, out_channels=64, kernel_size=3))


# Inputs to the model
x1 = torch.randn(1, 10, 5)
