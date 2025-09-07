
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        x1 = self.conv(x1)
        x1 = self.bn(x1)
        return x1


# Initializing the model
m = Model()
print(__output__.shape)  # (1, 4, 4, 20)
