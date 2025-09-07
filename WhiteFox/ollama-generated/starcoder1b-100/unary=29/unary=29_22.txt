
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=1.0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.clamp_min(v2, min_value)
        v4 = v2 - v3
        v5 = torch.clamp_max(v4, max_value)
        v6 = v3 + v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
