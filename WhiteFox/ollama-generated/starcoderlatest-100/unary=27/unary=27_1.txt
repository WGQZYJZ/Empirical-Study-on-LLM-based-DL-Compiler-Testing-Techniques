
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-6, max_value=10.0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v6


# Initialization of the model with a minimum value of 1e-6 and maximum value of 10
m = Model(min_value=1e-6, max_value=10.0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
