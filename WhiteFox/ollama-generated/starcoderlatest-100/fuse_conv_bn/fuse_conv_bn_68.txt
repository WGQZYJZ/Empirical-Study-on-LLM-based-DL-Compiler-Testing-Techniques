
class Model(torch.nn.Module):
    def __init__(self, stride=1):
        super().__init__()

        self.conv = torch.nn.Conv2d(3, 64, 7, stride)
        self.bn = torch.nn.BatchNorm2d(64, track_running_stats=True)

    def forward(self, x):
        y = self.conv(x)
        z = self.bn(y)
        return z
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
