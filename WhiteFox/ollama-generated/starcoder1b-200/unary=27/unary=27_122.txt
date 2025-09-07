
class Model(torch.nn.Module):
    def __init__(self, min_value=1, max_value=256):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        min_v = min_value
        max_v = max_value
        v2 = torch.clamp_min(v1, min_v)
        v3 = torch.clamp_max(v2, max_v)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
