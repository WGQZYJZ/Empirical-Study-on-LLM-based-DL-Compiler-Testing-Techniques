
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.125):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * self.negative_slope
        v3 = torch.where(v1, v1, v2)
        return v3


# Initializing the model with negative slope of 0.125
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
