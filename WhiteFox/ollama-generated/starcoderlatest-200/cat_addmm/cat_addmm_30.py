
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, m1, m2)
        v2 = torch.cat([v1], dim=1)
        return v2
 
