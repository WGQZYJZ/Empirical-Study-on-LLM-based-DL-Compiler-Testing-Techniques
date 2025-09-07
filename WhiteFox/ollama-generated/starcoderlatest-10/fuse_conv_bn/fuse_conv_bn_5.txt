
class Model(torch.nn.Module):
    def __init__(self, bn_eval=False):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=7)
        self.bn1   = torch.nn.BatchNorm2d(num_features=64, track_running_stats=False, eval=bn_eval)
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=5)
        self.bn2   = torch.nn.BatchNorm2d(num_features=32, track_running_stats=True, eval=bn_eval)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.bn1(self.conv1(x))), kernel_size=2)
        x = self.bn2(self.conv2(x))
        return x


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
