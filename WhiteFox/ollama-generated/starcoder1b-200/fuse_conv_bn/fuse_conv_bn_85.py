
class Model(torch.nn.Module):
    def __init__(self, num_channels=2):
        super().__init__()

        self.conv1 = torch.nn.ConvXd(1, num_channels, 3)
        self.bn = torch.nn.BatchNormXd(num_channels)

    def forward(self, x):
        output = self.bn(self.conv1(x))
        return output


# Initializing the model
m = Model()

__input__ = ... # Input tensor
