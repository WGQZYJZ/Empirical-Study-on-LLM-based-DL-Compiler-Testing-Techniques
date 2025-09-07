
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x, y):
        v1 = self.conv(x) * (y + 0.5)
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 * 1.386294361119895
        v5 = v4 + y
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
y = torch.randn(1, 3, 64, 64)
