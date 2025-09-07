
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=0):
        return torch.mm(x1, inp)


m = Model()
inp  = torch.randn(3, 5, requires_grad=True)
x1   = torch.randn(1, 8, 64, 64)
__output__  = m(x1, inp)
__output__.backward()


