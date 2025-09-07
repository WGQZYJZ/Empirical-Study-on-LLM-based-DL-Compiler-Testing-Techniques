
class Model(torch.nn.Module):
    def __init__(self, minval = 0., maxval=1.):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3,8,kernel_size=(5,7),stride=(1,2))
    
    def forward(self, x1):
        v1  = self.convT(x1)
        v2 = F.clamp_min(v1, minval=0.) # clamped min: 0
        v3 = F.clamp_max(v2, maxval=1.) # clamped max: 1 
        return v3


# Initializing the model