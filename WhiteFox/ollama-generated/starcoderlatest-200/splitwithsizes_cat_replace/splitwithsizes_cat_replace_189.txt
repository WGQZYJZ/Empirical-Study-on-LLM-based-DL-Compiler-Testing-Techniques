
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, 256, dim=0)
        c1 = torch.cat([s1[i] for i in range(len(s1))], dim=0)
        return c1
