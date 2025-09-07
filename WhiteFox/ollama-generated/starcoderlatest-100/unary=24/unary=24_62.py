
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        slope_term = v1 * negative_slope
        v2 = torch.where(mask, v1, slope_term)
        return v2


# Initializing the model with the specified negative slope
m = Model(negative_slope=0.001)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
