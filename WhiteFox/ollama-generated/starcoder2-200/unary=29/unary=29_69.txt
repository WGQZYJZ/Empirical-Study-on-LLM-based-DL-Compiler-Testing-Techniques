
class Model(torch.nn.Module):
    def __init__(self, minval=-10., maxval=255.):
        super().__init__()
        self.minv = float(minval)
        self.maxv  = float(maxval)
        self.convt = torch.nn.ConvTranspose2d(3, 8, 4, stride=4, padding=0)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = torch.clamp_min(v1, self.minv)
        v3  = torch.clamp_max(v2, self.maxv)
        return v3


# Initializing the model