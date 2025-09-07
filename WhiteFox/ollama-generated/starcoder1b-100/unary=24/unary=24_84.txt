
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    @torch.no_grad()
    def forward(self, x1, mask):
        v1 = self.conv(x1)
        v2 = v1 * negative_slope
        v3 = torch.where(mask > 0, x1, v2)
        return v3


# Inputs to the model
negative_slope = 1  # A constant
x1 = torch.randn(1, 3, 64, 64)
mask = x1 > 0  # A boolean mask
