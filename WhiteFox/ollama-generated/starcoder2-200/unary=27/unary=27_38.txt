

class Model(torch.nn.Module):
    def __init__(self, minval=0., maxval=10.)
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + minval
        v4  = max_value  - v1 
        v5  = torch.clamp(v3, 0., 1.)
        return v5

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
