
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None, x2=None, inp=30): 
        v = torch.mm(x1, x2) + inp # Matrix multiplication
        return v


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(4096, 50)
x2  = torch.randn(50, 8732)
__output__   = m(x1=x1, x2=x2)

