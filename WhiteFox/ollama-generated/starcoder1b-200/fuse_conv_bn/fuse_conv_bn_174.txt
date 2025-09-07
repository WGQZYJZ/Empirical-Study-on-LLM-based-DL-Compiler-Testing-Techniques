
class Model(torch.nn.Module):
    def __init__(self, feature_channels=2048):
        super().__init__()
        self.conv = torch.nn.ConvNd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormNd(...)  # X should match with ConvNd

        