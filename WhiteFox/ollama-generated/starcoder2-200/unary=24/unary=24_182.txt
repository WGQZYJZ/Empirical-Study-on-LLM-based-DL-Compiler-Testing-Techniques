
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() 
        v4  = -torch.ones_like(v1)*negative_slope*v2
        v3  = torch.where(v2, v1, v4)   
        return v3

# Initializing the model
m = Model(negative_slope=0.5)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
