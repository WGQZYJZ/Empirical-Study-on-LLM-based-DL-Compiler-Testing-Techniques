
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn  = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1)  # Permute the input tensor
        v2 = self.conv(v1)              # Perform convolution over each spatial dimension. 
        v2 = self.bn(v2)                  # Batch normalization of the convolution results.
        return v2


# Inputs to the model
x1 = torch.randn(1, 16, 48, 48)
