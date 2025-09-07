
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        clamped = torch.clamp_min(v1, min_value)
        clamped = torch.clamp_max(clamped, max_value)
        return clamped


# Initializing the model
m = Model(-0.5, 0.5)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
