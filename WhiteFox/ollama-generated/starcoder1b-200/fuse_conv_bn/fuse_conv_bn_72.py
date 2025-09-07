
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2 or 3 representing the dimension of input tensor
        self.bn  = torch.nn.BatchNorm2d(...) # X should match with Conv2d

    def forward(self, x):
        v  = self.conv(x)
        v  = self.bn(v)
        return v


# Inputs to the model
input_tensor = torch.randn(1, 3, 4, 4)
