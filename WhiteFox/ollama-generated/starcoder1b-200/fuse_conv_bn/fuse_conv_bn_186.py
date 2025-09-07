
class Model(torch.nn.Module):
    def __init__(self, x1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x2):
        x1 = x2.permute(0, 3, 1, 2)
        v1 = self.conv(x1)
        v2 = self.bn(v1)

        return v2


# Initializing the model
m = Model(torch.randn(1, 2, 2, 3))


