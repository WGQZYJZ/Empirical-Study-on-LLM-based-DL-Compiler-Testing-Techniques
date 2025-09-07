
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        negative_slope = negative_slope * torch.ones_like(v1)
 
        return torch.where(mask, v1, negative_slope)


# Initializing the model
m = Model(negative_slope=0.125)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
