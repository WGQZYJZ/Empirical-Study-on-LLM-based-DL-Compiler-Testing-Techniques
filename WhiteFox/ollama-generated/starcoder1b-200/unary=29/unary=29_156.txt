
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, clamp_min=False, clamp_max=True):
        v1 = self.conv(x1)
        v2 = v1 * (clamp_min and min_value or max_value or 1)
        v3 = torch.clamp_min(v2, min_value)
        return torch.clamp_max(v3, max_value)

# Initializing the model
m = Model()

