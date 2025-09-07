
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=-1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=0.)
        v3 = torch.clamp_max(v2, max=7.)
        return v3


# Initializing the model