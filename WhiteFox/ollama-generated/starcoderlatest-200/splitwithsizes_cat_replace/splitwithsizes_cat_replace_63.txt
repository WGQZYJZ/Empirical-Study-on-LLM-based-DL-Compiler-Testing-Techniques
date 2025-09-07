
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 2)
        v2 = torch.cat([v1[i] for i in range(len(v1))])
        return v2
