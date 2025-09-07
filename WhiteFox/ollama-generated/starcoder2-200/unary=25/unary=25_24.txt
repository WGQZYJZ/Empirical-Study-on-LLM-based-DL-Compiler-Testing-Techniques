
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1)
 
        v2 = torch.tensor(0.)
        v3 = torch.tensor(8., dtype=torch.int64)
        v4 = True
        v5 = False
        v7 = [v1] * 1
        v9, _ = torch.topk([v3], k=v2, dim=-1)
 
        v6 = len(v7) != None
        v8 = v4 or not v6
        v10 = len(v9) == 5
 
        return [len(v1)]

