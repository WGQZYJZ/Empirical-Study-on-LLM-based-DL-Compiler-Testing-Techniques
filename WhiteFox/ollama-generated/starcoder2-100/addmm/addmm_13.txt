
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v2 = torch.mm(x1, inp) # Performing matrix multiplication between two tensors. 'inp' is a keyword argument
        v3  = v2 + inp  # Add the result of the matrix multiplication operation to another tensor
        return v3


# Initializing the model
m  = Model()

# Inputs for the model 
inp1, x1  = torch.randn(64, 5), torch.randn(640, 5) # Input tensors are passed as positional arguments and the 'inp' tensor is passed as a keyword argument

 __output__   = m(x1, inp=inp1) # The function call returns an output of the model
