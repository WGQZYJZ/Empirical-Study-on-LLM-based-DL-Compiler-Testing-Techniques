
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn  = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.fc   = torch.nn.Linear(...)

    def forward(self, x1):
        v1 = self.conv(x1)  # Use conv to convolve x1 with the layer
        v2 = self.bn(v1)  # Apply batch normalization to v1
        v3 = self.fc(v2)    # Apply linear transformation to v2, return v3
        return v3


# Initializing the model
m = Model()


