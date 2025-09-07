
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)  # Permute the input tensor
        v2 = self.conv(v1)        # Perform convolution using this permuted tensor
        v3 = self.bn(v2)          # Perform batch normalization
        return v3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
