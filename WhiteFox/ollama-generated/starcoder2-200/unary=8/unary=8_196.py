

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x):
        v1  = self.convT(x) 
        v2  = v1 + 3  
        v3  = torch.clamp(v2, min=0)
        v4  = torch.clamp(v3, max=6)
        v5  = v1 * v4
        v6  = v5 / 6  
        return v6

m  = Model()
x = torch.randn(1, 8, 29, 29)

__output__  = m(x)

