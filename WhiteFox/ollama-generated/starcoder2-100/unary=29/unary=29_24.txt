
class Model(torch.nn.Module):
    def __init__(self, minv = -10., maxv = 43258769):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(
            3, 8, kernel_size= 3, stride= 1, padding= 1)
 
        self.minv = minv
        self.maxv = maxv
 
    def forward(self, x):
        v1  = self.convt(x)
        v2  = torch.clamp_min(v1, self.minv) # clamped output
        v3  = torch.clamp_max(v2, self.maxv) # clamped output after previous operation
 
        return v3
