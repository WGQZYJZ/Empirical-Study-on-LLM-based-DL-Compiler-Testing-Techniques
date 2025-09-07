
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        v2 = v1 + inp
        return v2

 # Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(100, 3, 64, 64)
inp = torch.randn(3, 64, 64)
