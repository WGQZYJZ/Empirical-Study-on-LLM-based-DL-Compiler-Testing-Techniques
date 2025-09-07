
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.mm(x1, x2) + x3


m = Model()
x1 = torch.randn(2, 2, 64, 64)
x2 = torch.randn(2, 2, 64, 64)
inp = torch.randn(2, 2, 64, 64)
