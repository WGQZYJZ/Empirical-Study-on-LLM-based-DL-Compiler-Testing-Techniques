
class Model(torch.nn.Module):
    def __init__(self, min_value=0.3, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.clamp_min(v2, kwargs['min_value'])
        v4 = torch.clamp_max(v3, kwargs['max_value'])
        return v4

# Initializing the model
m = Model(min_value=0.1, max_value=0.9)


