
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, inp=None):
        v1 = self.conv(x1)
        if inp is None:
            return v1
        else:
            v2 = torch.mm(v1, inp) + inp
            return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(8, 3, 32, 32)
inp = torch.randn(8, 3, 1, 1)
