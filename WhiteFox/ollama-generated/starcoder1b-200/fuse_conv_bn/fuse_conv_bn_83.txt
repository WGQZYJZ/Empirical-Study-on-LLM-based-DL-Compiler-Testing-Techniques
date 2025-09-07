
class Model(torch.nn.Module):
    def __init__(self, bn_track_stats=False):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        if bn_track_stats:
            self.bn1 = torch.nn.BatchNormXd(...)

    def forward(self, x):
        output = self.conv1(x)
        if self.bn1.training and self.bn1.is_training():
            output = self.bn1(output)
        return output


# Initializing the model
m = Model()


