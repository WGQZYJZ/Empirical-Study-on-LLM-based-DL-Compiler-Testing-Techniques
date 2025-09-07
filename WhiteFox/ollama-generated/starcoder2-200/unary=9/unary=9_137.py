
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
 
    def forward(self, x):
      v1 = self.conv(x)
      v2 = v1 + 3
      v3 = torch.clamp_min(v2, min=(0)) # clamp the addition operation to a minimum of 0
      v4 = torch.clamp_max(v3, max=6)# clamp the previous operation to a maximum of 6
      return v4/6

m = Model()
