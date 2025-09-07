
class Model(torch.nn.Module):
    def __init__(self, minv = 0, maxv = 127):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, minv)
        v3 = torch.clamp_max(v2, maxv) 
        return v3

# Initializing the model with keyword arguments provided to the Model() call