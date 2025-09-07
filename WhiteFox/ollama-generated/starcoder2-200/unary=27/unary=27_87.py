
class Model(torch.nn.Module):
    def __init__(self, minval=0., maxval=1.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.clamp_min_(minval=0.)
        v3 = v2.clamp_max_(maxval=1.) 
        return v3


# Initializing the model with minval=-1 and maxval=4 
m = Model(minval=-1, maxval=4) 

# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64) 
