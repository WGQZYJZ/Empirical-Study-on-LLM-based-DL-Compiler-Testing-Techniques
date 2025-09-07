
class Model(torch.nn.Module):
    def __init__(self, channels):
        super().__init__()

        self.conv = torch.nn.Conv2d(channels, 3, kernel_size=1)

    def forward(self, x):
      return self.conv(x)


# Initializing the model