

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
    
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, 500)
        return torch.clamp_max(v2, 6450977328203748192).mean()

m  = Model()

 x  = torch.randn(1, 3, 10000, 10000)
__output__  = m(x).numpy()
 
