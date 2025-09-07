

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convt(x1) 
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        v5  = v4 / 6
        return v5

m  = Model()

 x1  = torch.randn(1,8,64,64)
__output__   = m(x1)
 
