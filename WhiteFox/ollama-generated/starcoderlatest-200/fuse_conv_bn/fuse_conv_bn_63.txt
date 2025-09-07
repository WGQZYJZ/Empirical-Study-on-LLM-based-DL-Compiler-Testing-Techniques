
class ConvNet(torch.nn.Module):
    def __init__(self, num_features: int = 64) -> None:
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=num_features, kernel_size=(3,3))

    def forward(self, x):
        x = self.conv1(x)  # ConvXd

        return x

# Initializing the model
m = ConvNet()


