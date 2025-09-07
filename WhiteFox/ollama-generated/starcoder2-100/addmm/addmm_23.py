
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear()
 
    def forward(self, x1, inp=None):
        v1  = mm(x1, inp)
        v2  = v1 + inp
        return v2

m = Model()
__output__  = m(x1, inp)
