
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v2 = torch.mm(x1, inp)  # Perform matrix multiplication on two input tensors using a keyword argument 
        v3 = v2 + inp   # Add the result of the matrix multiplication to another tensor with a constant value
        return v3

# Initializing the model
m = Model()
 
__output__  = m(torch.randn(5, 4), torch.randn(5))

