
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor = None):
        super().__init__()
        self.inp = torch.nn.Parameter(inp)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) # Perform matrix multiplication on two input tensors
        v2  = v1 + self.inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m = Model(torch.randn(1, 8, 64, 64))

# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
