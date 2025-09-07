
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
inp  = torch.randn(10, 20, 3) # A tensor for keyword argument 'inp'
x1   = torch.randn(5,  8, 64, 64)
