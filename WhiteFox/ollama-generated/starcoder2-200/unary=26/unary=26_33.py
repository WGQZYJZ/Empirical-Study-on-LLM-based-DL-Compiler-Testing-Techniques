
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3,8,1,stride=1, padding=0)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convt(x1) 
        v2  = (v1 > 0).float()
        v3  = -v1 * torch.abs(self.negative_slope)
        v4  = torch.where(v2 ==  1., v1, v3)
        return v4


# Initializing the model
m  = Model(-5.)

# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
__output__  = m(x1)



