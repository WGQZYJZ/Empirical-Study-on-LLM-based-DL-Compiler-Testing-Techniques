
class Model(torch.nn.Module):
    def __init__(self, channels: int = 32, kernel_size: Tuple[int, ...] = (3,)):
        super().__init__()

        self.conv = torch.nn.Conv1d(channels, 64, kernel_size)
        self.bn   = torch.nn.BatchNorm1d(64)

    def forward(self, x):
        y = self.conv(x)
        z = self.bn(y)

        return z


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 32, 64)
