
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 10, kernel_size=5)
        self.bn = torch.nn.BatchNorm2d(10, track_running_stats=True)

    def forward(self, x):
        v1 = self.bn(torch.nn.functional.conv2d(x, self.conv.weight))
        return v1

# Initializing the model
m  = Model()

