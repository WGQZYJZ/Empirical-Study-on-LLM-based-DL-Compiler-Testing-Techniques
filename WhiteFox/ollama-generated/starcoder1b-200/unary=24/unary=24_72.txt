
class Model(nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v = self.conv(x)
        v = torch.where(v > 0, v * -self.negative_slope, v)
        return v


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
