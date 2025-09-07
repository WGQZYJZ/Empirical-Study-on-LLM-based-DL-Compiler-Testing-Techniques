
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...)
        self.relu = torch.nn.ReLU(...)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 1, 2)
        v2 = self.conv(v1)
        v3 = self.bn(v2)
        v4 = self.relu(v3)
        return v4


# Inputs to the model
x1 = torch.randn(1, 2, 3, 2)
