
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1)
        v2 = self.conv(v1).view(v1.shape[0], -1)
        return self.bn(v2)


# Initializing the model
m = Model()


