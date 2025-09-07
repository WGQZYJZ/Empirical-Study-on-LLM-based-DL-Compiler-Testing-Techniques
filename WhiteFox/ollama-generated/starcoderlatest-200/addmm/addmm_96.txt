
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
        if inp is not None:
            self.inp = torch.nn.Parameter(input_tensor)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2 = v1 + self.inp # Add the result of the matrix multiplication to another tensor 'self.inp'
        return v2


# Initializing the model with an input tensor as a parameter
m = Model(input_tensor)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
