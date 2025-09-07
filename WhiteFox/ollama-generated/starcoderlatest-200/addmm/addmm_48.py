
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp=None):
        x1 = torch.randn(1, 32, 56, 56)
        t1 = torch.mm(x1, x1)
        t2 = t1 + inp
        return t2


# Inputs to the model
inp = torch.randn(1, 32, 32)
