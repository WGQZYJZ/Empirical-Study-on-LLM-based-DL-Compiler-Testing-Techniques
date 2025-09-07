
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.split(x1, [2], 0)
        v4  = torch.cat([v3[i] for i in range(len(v3))], 0)
#        return True
        return v4

