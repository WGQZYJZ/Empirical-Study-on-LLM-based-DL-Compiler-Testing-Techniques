
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...)
        self.bn    = torch.nn.BatchNorm1d(...)

    def forward(self, x):
        v = x.permute(0, 2, 3, 1)
        v = self.conv(v)
        return self.bn(v)


# Initializing the model
m = Model()


