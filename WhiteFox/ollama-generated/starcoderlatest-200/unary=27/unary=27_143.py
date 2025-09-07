
class Model(torch.nn.Module):
    def __init__(self, min_value=-10., max_value=10.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        min_value = -10. # Minimum value is a keyword argument
        max_value = 10. # Maximum value is a keyword argument
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
