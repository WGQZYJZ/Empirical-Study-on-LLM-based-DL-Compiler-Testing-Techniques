
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2) * 0.5
        v3 = torch.erf(v2 / 0.7071067811865476) + 1
        v4 = (v1 * v3).softmax(-1)
        return v4


# Initializing the model
m = Model()
x1, x2 = torch.randn(1, 3, 64, 64), torch.randn(1, 3, 64, 64)
