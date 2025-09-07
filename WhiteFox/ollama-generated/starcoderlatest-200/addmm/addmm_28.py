
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp = None):
        if inp is None:
            v1 = torch.mm(x1, x1)
        else: 
            v2 = torch.mm(x1, x1) + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
inp  = torch.randn(1, 3, 64, 64)
x1 = torch.randn(1, 3, 64, 64)
