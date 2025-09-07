
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        if x2:
            v1 = torch.mm(x1, x2)
        else: 
            v1 = torch.mm(x1, x1)
        v2 = v1 + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 5760, 2048, 3) # A non-optional keyword argument is passed
