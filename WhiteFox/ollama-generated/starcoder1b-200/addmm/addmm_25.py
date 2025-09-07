
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=torch.zeros((1, 2, 3))):
        v1 = torch.mm(x1, x1)
        v2 = v1 + inp
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp  = torch.zeros((1, 2, 3))
