
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v2 = torch.mm(x1, 0) + inp
        return v2
 
 
m  = Model()
 
__output__  = m(torch.randn(8), torch.randn(9))

