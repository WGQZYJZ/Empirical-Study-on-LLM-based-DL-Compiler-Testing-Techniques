

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
        v0 = x1
        v1 = self.conv(v0)
        v2 = torch.clamp_min(v1,-0.5)
        v4 = torch.clamp_max(v2,0.987654321)
return  v4
