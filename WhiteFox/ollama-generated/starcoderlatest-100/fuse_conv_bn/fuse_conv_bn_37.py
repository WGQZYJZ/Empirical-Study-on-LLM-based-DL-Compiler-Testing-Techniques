 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3)
        self.bn = torch.nn.BatchNorm2d(1, track_running_stats=False)

    def forward(self, x1):
        x2 = self.conv(x1)
        y1 = self.bn(x2)
        return y1

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
