
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd

        # Only fuse the batch normalization layer if it is a tracking running statistics 
        self._fuse_if_track_running_stats = False

    def forward(self, x):
        y = self.conv(x)
        if self._fuse_if_track_running_stats:
            z = self.bn(y)
        else:
            z = self.bn(y, 1)
        return z


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 3, 64, 64)
