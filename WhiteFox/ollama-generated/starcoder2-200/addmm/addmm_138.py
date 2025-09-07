
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2) # Performing matrix multiplication operation
        v2 = v1 + 1 if not x2 is None else 0
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(32, 32)
x2 = torch.randn(32,) if not x2 is None else None # Input tensor  'x2' is optional
 
 __output__  = m(x1, x2=None)

