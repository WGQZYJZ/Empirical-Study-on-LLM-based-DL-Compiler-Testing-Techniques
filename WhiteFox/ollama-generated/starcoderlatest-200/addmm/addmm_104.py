
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp = None):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 64, 64)
__output__  = m(x1, x2)

