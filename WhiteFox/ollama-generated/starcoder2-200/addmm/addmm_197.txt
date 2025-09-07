
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        return v1 + 0.5


# Initializing the model
m  = Model()

# Inputs to the model
x2 = torch.randn(3, 8) # Input tensor 2
inp = torch.randn(4, 9) # Keyword argument 'inp'
 
 