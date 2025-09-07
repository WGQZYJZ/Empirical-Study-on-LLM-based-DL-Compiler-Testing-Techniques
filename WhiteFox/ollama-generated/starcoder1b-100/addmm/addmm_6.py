
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v = torch.mm(x1, inp) + inp
        return v


m = Model()
inp1 = torch.randn(1, 3, 64, 64)
inp2 = torch.randn(1, 5, 64, 64)
