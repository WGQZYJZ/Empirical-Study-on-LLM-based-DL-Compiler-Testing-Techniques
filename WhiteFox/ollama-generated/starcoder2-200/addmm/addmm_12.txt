
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, inp): # Note that we pass the 'inp' tensor here!
        v = torch.mm(x1, x2) + inp  # Add the result of a matrix multiplication to another tensor 
        return v

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(50, 64, 64, 3)
__output__  = m(x1)

