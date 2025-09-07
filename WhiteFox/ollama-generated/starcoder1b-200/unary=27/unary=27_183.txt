
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=200):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

# Initializing the model
m = Model(min_value=1e-5, max_value=200)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
