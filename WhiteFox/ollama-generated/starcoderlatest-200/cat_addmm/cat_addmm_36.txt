
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, self.A, self.B)
        v2 = torch.cat([v1], dim=1)
        return v2
