
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1:torch.Tensor, inp:torch.Tensor) -> torch.Tensor:  # Input1 and Input2 are keyword arguments that take Tensor objects as input.
        t1 = torch.mm(x1, inp) 
        t2 = t1 + inp
        return t2

# Initializing the model 
m = Model()
 
# Inputs to the model
inp = torch.randn(3, 64) # A randomly generated Tensor of size (3 x 64).
x1 = torch.randn(30, 58, 64, 92) # A randomly generated Tensor of size (30 x 58 x 64 x 92).
 
# Output from the model
__output__  = m(x1, inp)

