
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15968723504907807):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        m1 = (v1 > 0).float()
        v2 = v1 * negative_slope
        v3 = torch.where(m1, v1, v2)
        return v3


# Initializing the model
m  = Model(negative_slope=0.15968723504907807)


# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
__output__  = m(x1)