
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 5 * 6
        v3 = torch.clamp_min(v2, 1)
        v4 = torch.clamp_max(v3, 7)
        v5 = v1 * v4
        v6 = v5 / 8
        return v6

# Initializing the model