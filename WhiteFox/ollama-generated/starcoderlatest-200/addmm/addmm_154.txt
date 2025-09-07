
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) + inp
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(8, 64)
inp = torch.randn(32, 64)
