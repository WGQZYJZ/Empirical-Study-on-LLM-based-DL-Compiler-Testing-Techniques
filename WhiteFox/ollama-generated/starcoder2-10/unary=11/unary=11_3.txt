
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Clamp minimum of zero 
        v4  = torch.clamp_max(v3, 6)
        v5  = v4 / 6
__output__  = v5

