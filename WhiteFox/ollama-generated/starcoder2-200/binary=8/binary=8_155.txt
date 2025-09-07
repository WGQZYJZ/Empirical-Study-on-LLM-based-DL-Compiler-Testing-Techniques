
class Model(torch.nn.Module):
    def __init__(self, o):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.o = o

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.o
        return v2


m  = Model(torch.zeros(4))

x1 = torch.randn(3, 8, 65, 70)
