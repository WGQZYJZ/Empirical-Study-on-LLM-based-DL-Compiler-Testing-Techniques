
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v1 = torch.clamp_min(v0, min=1)
        return torch.clamp_max(v1, max=4)

# Initializing the model