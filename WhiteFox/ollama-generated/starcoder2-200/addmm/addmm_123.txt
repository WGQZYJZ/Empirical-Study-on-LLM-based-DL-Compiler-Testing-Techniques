
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2)
        return v1 + 0
 

