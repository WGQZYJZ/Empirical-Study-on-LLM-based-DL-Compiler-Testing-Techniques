
class Model(torch.nn.Module):
    def __init__(self, minValue=0., maxValue=1.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernelSize=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, minValue)
        v3 = torch.clamp_max(v2, maxValue)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
__output__  = m(x1)