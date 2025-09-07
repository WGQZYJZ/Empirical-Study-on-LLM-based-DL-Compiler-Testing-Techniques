
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 + 3
        return torch.clamp_min(v2, 0), torch.clamp_max(v2, 6), v2 / 6


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
__output__[0], __output__[1], __output__[2] = m(x)


