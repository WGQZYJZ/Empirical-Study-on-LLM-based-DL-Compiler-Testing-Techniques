
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        slope = -self.negative_slope * torch.ones_like(mask).to(dtype=torch.float32)
        value = torch.where(mask == 1, v1, slope)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
