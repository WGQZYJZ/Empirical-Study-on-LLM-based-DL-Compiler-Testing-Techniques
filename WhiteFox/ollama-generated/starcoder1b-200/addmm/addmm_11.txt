
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=0):
        v1 = torch.mm(x1, input2)
        v2 = t1 + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
inp  = torch.randn(1, 8, 64, 64)
__output__  = m(x1, inp)


