
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)

    def forward(self, x2):
        v2 = self.conv(x2)
        v3 = v2 * negative_slope
        v4 = torch.where(v2 > 0, v2, v3)
        return v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 8, 64, 64)
