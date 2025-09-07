
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1  = x1.permute(0, 3, 1, 2)
        v2  = self.conv(v1)
        bn  = self.bn(v2)
        return bn


# Inputs to the model
x1 = torch.randn(1, 3, 3, 64) # X should match with ConvXd
