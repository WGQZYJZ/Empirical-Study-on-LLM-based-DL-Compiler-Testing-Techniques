
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, -1 * self.negative_slope * v1, v1)
        v3 = v2 * (2 * self.negative_slope / 3 + 1)
        v4 = torch.where(torch.abs(v3) > 1e-5, torch.zeros_like(v3), v3)
        return v4


# Initializing the model
m = Model(-0.7964000889327087)
x1 = torch.randn(1, 3, 64, 64)
