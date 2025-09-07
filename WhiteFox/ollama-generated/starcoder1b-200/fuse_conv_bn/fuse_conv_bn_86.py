
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 2 or 3 representing the dimension of input_tensor
        self.bn = torch.nn.BatchNorm2d(...) # X should match with Conv2d
    def forward(self, x):
        v = self.bn(self.conv(x))
        return v


# Initializing the model
m = Model()


__input__ = torch.randn(1, 3, 5, 5)
