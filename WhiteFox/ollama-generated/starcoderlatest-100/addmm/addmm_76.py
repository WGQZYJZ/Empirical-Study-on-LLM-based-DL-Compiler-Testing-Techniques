
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        inp = torch.randn(10)
        v1  = torch.mm(x1, inp)
        v2 = v1 + inp # Pass 'inp' as a keyword argument
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10)
inp = torch.randn(10)
