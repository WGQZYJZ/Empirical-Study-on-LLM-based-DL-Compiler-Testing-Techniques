
class Model(torch.nn.Module):
    def __init__(self, min=0., max=128):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min)
        v3  = torch.clamp_max(v2, max) 
        return v3
