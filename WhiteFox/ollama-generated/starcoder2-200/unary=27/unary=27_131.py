
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.) # clamping min value as 0 to avoid Nan/Inf
        v3  = torch.clamp_max(v2, max=15) # clamping max value to 15 to avoid Nan/Inf
        return v3

# Initializing the model