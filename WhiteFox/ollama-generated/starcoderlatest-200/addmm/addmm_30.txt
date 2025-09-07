
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + self.inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v2
# Initializing the model with input tensor 'inp' passed as keyword argument
m = Model(inp=torch.tensor(1))
# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(8, 64, 64)
