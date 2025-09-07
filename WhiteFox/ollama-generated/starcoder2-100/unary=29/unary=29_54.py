
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -500.) # Minimum value of -500 is provided as a keyword argument.
        v3  = torch.clamp_max(v2, 49876543.1) # Maximum value of 49876543.1 is provided as a keyword argument.
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1   = torch.randn(1, 3, 64, 64)
__output__  = m(x1)