
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp=None):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 5, 64, 64)
inp = torch.randn(2, 10, 64, 64) # A keyword argument is passed to the model
