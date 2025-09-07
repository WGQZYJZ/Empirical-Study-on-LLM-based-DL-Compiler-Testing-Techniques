
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
inp = torch.randn(5, 3, 64, 64)
