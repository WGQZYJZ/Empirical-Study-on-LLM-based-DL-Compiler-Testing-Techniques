
class Model(torch.nn.Module):
    def __init__(self, minval=-10000, maxval=32767):
        super().__init__()
        self.conv  = torch.nn.Conv2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, minval) 
        v3  = torch.clamp_max(v2, maxval)  
        return v3


# Initializing the model
m = Model(-50, -49)

 # Inputs to the model
x1  = torch.randn(1, 8, 64, 64)

 