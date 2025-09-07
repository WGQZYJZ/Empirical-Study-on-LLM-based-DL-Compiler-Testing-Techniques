
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn   = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.conv(v1)
        v3 = self.bn(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
