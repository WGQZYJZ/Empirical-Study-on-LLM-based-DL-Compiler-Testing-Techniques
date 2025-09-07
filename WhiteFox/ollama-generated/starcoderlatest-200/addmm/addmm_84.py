
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, x1)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn(100)
x1  = torch.randn(100, 3, 64, 64)
