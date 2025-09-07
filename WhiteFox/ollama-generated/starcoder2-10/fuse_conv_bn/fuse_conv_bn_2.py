
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 4, 3) # Conv2d layer
        self.bn   = torch.nn.BatchNorm2d(4) # BN2d layer

    def forward(self, x):
        return self.bn(torch.nn.functional.conv2d(x, self.conv))

m  = Model()
x1 = torch.randn(80, 3, 769, 75)
