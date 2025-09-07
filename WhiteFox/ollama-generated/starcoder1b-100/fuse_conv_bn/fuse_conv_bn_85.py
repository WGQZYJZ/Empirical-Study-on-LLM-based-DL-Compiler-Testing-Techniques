
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = self.bn(v1)
        return v2


# Initializing the model
m = Model()

