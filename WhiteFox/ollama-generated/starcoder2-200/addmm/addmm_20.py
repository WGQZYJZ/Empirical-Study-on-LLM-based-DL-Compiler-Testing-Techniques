
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) # matrix multiplication of two input tensors
        v2 = v1 +  input  # Add the result of the matrix multiplication to another tensor 'input'
        return v2

# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(4,5)
inp    = torch.randn(5,8).detach() # Detach the tensors from the computational graph.
__output__  = m(x1=input1, inp=inp)

