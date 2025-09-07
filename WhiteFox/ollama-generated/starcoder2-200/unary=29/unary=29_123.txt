

class Model(torch.nn.Module):
    def __init__(self, min_value=-10., max_value=10.):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 4)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, min=min_)
        v3  = torch.clamp_max(v2, max_=max_)
        return v3


m  = Model()
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


