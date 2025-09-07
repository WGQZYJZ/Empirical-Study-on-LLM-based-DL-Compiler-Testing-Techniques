
class Model(torch.nn.Module):
    def __init__(self, max_, min_):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, max_) # Min: 0.5
        v3  = torch.clamp_max(v2, min_) # Max: -0.4 
        return v3

# Initializing the model
max_  =  1
min__ =  -1
m     = Model(max_, min__)


# Inputs to the model
x1    = torch.randn(1, 3, 64, 64)
