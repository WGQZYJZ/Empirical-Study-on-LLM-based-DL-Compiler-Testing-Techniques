
class Model(torch.nn.Module):
    def __init__(self, min=0., max=500.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2_min    = torch.clamp_min(v1, min=0.) # Clamp the output of the convolution to a minimum value
        v3_max    = torch.clamp_max(v2_min, max=500.)  # Clamp the output of the previous operation to a maximum value
        return v3_max


# Initializing the model
m = Model()
 
 # Inputs to the model
x1   = torch.randn(1, 3, 64, 64)
 
