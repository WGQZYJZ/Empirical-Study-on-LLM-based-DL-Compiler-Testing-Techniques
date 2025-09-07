
class Model(torch.nn.Module):
    def __init__(self, minv=1., maxv=250.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.minval = minv
        self.maxval = maxv
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.minval)
        v3 = torch.clamp_max(v2, self.maxval)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)