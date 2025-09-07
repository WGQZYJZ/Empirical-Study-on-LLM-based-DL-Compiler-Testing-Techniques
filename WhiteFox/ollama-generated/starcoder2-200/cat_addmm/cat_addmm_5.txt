
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1):
        t2  = torch.cat([x1], dim) 
        return t2

