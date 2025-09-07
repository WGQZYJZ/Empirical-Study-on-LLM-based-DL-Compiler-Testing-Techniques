
class Model(torch.nn.Module):
    def __init__(self, negative_slope=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (x1 < 0).any(dim=(0))
        v2 = torch.where(mask, v1 * self.negative_slope, v1)
        v3 = v2  + 1
        v4 = v2 * v3
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
