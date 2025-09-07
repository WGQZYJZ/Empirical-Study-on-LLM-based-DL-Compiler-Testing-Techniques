
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 2, or 3 representing the dimension of input_tensor
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        x2  = self.conv(x1)  # x2 is a fused convolution layer
        x3  = self.bn(x2)     # x3 is a batch normalization layer
        return x3


# Initializing the model
m = Model()
input_tensor = torch.randn(1, 1, 84, 96)
