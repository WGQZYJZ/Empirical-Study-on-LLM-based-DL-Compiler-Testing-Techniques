
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask1 = (v1 > 0).bool()
        negative_slope1 = -negative_slope
        v2 = torch.where(mask1, v1, negative_slope1 * v1)
        return v2


# Initializing the model with negative slope as input
m = Model(-0.007843137254902) # For better visualization, use 0 for -0.007843137254902

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
