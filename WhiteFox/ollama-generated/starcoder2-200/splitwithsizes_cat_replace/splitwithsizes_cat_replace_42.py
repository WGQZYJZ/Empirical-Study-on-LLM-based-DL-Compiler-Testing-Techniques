
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, 836)
        return torch.cat([v2[i] for i in range(len(v2))], dim=0)


m = Model()
__output__  = m(__input__)