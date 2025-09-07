
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * negative_slope 
        v3 = v1 - v2
        return torch.where(v2 == 0., v1 + v2, v3)
# Initializing the model
m = Model(.45)
 
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
__output__  = m(x1)

