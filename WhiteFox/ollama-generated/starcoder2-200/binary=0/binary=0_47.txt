
class Model(torch.nn.Module):
    def __init__(self, c2=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(c1, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


m1 = Model()

x1 = torch.randn(1, c1, 64, 64)
__output___m1 = m1(x1)


m2 = Model(c2=3)

x2 = torch.randn(1, 3, 64, 64)
__output___m2 = m2(x2)

print(__output___m1.shape, __output___m2.shape)

