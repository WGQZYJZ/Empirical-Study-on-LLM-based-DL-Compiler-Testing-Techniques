
class Model(torch.nn.Module):
    def __init__(self, min_value=1.0, max_value=2.0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return torch.clamp_min(torch.clamp_max(v6, min_value), max_value)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
