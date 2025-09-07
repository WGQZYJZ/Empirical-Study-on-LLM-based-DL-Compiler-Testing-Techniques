
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...) # X should match with Conv2d

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 50, 50) # (1, 3, 224, 224)
