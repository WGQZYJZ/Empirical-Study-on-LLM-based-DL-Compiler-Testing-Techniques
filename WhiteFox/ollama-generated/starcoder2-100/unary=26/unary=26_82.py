
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = (v1 > 0).float()
        v4  = -v2 * negative_slope + ((-negative_slope <= v1) & (v1 < 0)) 
        return torch.where(v2, v1, v4)

# Initializing the model
m = Model(-0.5)

# Inputs to the model
x1  = torch.randn(32, 8, 64, 64)
__output__  = m(x1)
