
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = torch.mm(x1[0], x1[3]) 
        v2  = torch.mm(x1[4], x1[6])     
        return v0 + v2


m = Model()

