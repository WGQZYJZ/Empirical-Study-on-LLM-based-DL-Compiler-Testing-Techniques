
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1)
        v2 = v1 + self.inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 3)
