
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2  = F.interpolate(v1, size=(64,)) # Apply the interpolation operation on the output of the convolution
        v3 = torch.clamp_min(v2, min=0.) 
        v4 = torch.clamp_max(v3, max=255.)
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

__output__   = m(x1)