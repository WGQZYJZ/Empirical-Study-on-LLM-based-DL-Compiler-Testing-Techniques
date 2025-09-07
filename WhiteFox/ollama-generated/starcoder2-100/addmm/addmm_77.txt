
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        v1 = torch.mm(x1, x2) # The matrix multiplication is performed on two input tensors 'x1' and 'x2'.
        v2  = v1 + x2
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 50)
inp = torch.randn(4, 90)
__output__  = m(x1, inp)

