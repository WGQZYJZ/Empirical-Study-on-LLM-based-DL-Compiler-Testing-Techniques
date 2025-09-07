
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min(-0.5))
        v3 = torch.clamp_max(v2, max(8.0))
        return v3


# Initializing the model with a specific minimum and maximum value
minval  = -7
maxval  = 100
m = Model()
 
# Inputs to the model for which we want to test the pattern
x1 = torch.randn(4, 3, 64, 64)
 
 
# Applying the model on input x1
__output__  = m(x1)

