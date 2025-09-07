
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp=0):
        v1 = torch.mm(x1, x2) + inp
        return v1


m = Model()
