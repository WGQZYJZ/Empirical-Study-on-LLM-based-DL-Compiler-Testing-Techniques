
class Model(torch.nn.Module):
    def __init__(self, minv=0., maxv=-1.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.) # Clamp the output of the convolution to a minimum value
        v3  = torch.clamp_max(v2, max=-1.) # Clamp the output of the previous operation to a maximum value
        return v3
# Initializing the model with initial values for the minimum and maximum values.
m = Model(minv=0., maxv=-1.)
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
