
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = F.relu(self.conv(x1)) 
        v2 = torch.clamp_min(v1, min_value=0.0, max_value=0.7853981633974483) # Minimum and maximum values: 0.0 and 0.7853981633974483
        v3 = torch.clamp_max(v2, min_value=0.33267134327394177, max_value=0.9999999403953552)
        return v3

