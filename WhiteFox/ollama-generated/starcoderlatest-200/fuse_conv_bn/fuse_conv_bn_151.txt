
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 10, kernel_size=(3, 5))
        self.bn = torch.nn.BatchNorm2d(10)

    def forward(self, x1):
        v1 = self.conv(x1).permute(0, 2, 3, 1).contiguous()
        v2 = self.bn(v1).contiguous()
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4, 5)
