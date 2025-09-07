
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope # Where v2 is True, multiply v1 by the negative slope. Where v2 is False, leave v1 unchanged.
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

# Generating a valid output
__output__  = m(x1)