
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)

    def forward(self, x):
        v = self.conv(x)
        return torch.where(v > 0, v, (v * -self.negative_slope))


# Inputs to the model
__input__ = torch.randn(2, 8, 32, 32)
m = Model()
output = m(__input__)

