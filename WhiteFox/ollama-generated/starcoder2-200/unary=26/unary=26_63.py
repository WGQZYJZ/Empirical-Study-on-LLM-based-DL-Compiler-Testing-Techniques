
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = (v1 > 0).float() 
        v3 = negative_slope * v2 
        v4 = torch.where(v2 ,v1, v3)
        return v4

# Initializing the model
m = Model().cuda(device=0)
m.apply(weights_init)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).cuda()
__output__  = m(x1)
