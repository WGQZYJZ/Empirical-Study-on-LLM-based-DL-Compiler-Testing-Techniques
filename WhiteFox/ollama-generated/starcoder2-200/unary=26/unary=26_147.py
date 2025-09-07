
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.convtranspose  = torch.nn.ConvTranspose2d(8, 16, 5)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = (v1 > 0).float() * self.negative_slope + torch.ones_like(v1).cuda().float()
        v3  = -torch.log(v1/v2)
        return v3

# Initializing the model
m  = Model(-0.75) # Here negative slope is -0.75 for demonstration purpose

# Inputs to the model
x1  = torch.randn(8, 4, 64, 64).cuda()
__output__  = m(x1)

