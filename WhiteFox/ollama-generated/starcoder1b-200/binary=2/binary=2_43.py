
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 - self.conv(other)


# Initializing the model with different inputs to generate the outputs
m  = Model()
x1 = torch.randn(3, 2, 64, 64)
x2 = torch.randn(1, 1, 1, 64)
y1 = m(x1)
y2 = m(x2)

