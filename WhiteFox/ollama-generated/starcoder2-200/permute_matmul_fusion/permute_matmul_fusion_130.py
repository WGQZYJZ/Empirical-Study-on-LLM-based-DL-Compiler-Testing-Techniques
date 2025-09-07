
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute([0, 2, 1]) # permute tensor A 
        v3  = torch.bmm(v1, x2)
        return v3

m = Model()
x1 = torch.randn(5, 2, 4)
x2 = torch.randn(5, 2, 3)
__output__= m(x1, x2)

