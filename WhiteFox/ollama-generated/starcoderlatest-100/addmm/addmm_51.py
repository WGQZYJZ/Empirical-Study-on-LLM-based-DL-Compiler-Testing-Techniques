
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inp=None):
        v1 = torch.mm(x1, x2)
        if inp:
            v2 = v1 + inp
        else:
            v2 = v1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
inp = torch.ones(1, 3, 64, 64)
