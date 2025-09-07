
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn  = torch.nn.BatchNorm2d(...)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1  = torch.cat([x1, x1], dim=1)
        v1 = self.conv(v1)
        v1 = self.bn(v1)
        v1 = self.relu(v1)
        return v1


# Inputs to the model
x1 = torch.randn(2, 3, 56, 37)
