
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3  = v1 + v2
        return v3


m = Model()
__output__  = m(
    torch.randn(10, 16), 
    torch.randn(16, 5), 
    torch.randn(10, 5), 
    torch.randn(16, 2))