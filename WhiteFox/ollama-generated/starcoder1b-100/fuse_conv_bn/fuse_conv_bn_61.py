
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x1):
        x2 = self.conv(x1)  # Apply convolution to the input tensor
        v2 = self.bn(x2)  # Batch normalization layer follows this convolution
        return v2


# Initializing the model
m = Model()


