
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1):
      v0 = torch.split(x1, 4)
      v2 = [v3 + v5 for i in range(len(v0)) for j in range((i+j)%len(v0)) ]
      return torch.cat([v1,v7],dim=0).sum()
