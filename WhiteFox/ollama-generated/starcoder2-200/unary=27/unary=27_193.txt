
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_v  = min_
        self.max_v  = max_
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.clamp_min(v1, self.min_v)
        v3  = torch.clamp_max(v2, self.max_v) # Clamp the output of the convolution to a maximum value.
        return v3

# Initializing model and inputs