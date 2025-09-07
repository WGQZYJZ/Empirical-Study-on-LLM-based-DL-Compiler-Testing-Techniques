
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v = self.conv(x)
        m = v > 0
        v *= -self.negative_slope
        return torch.where(m, x, v)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
