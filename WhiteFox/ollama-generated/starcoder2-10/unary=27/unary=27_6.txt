
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.clamp_min(v1, min=-4.) # clamping the minimum value of -4 to 0.5
        return torch.clamp_max(v2, max=789.)
 


m  = Model()
x1 = torch.randn(32, 3, 64, 64)
__output__  = m(x1)
 
