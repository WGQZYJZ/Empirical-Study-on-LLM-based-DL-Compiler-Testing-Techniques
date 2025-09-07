
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1):
 
        def fn():
            return torch.split(x1, 32*8, dim)
        v = fn()
        return tuple([i*5 for i in v])

# Initializing the model
m = Model(0)

 # Inputs to the model
x1 = torch.randn(127, 49)
__output__  = m(x1).sum()
 

