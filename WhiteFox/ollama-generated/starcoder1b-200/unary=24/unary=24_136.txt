
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0.0, v1 * 0.5, v1 * -self.negative_slope)
        v3 = torch.where(v1 > 0.0, v1 * 0.7071067811865476, v1 * -self.negative_slope)
        v4 = torch.where(v2 < 1.0, v1, v3)
        return v4

# Initializing the model
m = Model(negative_slope=-1.)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
