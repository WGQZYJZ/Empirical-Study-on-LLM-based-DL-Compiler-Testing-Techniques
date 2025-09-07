
class Model(torch.nn.Module):
    def __init__(self, maxv=50):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=0.5)
        v3 = torch.clamp_max(v2, max=49)  # clamped to the maximum value of 49
        return v3


# Initializing the model with the minimum and maximum values as keyword arguments
m = Model(minv=10, maxv=50)


