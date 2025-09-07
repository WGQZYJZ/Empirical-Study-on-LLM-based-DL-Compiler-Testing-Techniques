
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)  # Matrix multiplication between 'inp' and the first input tensor 'x1'
        v2 = v1 + inp           # Add result of matrix multiplication to another tensor
        return v2

# Initializing model
m = Model()

# Inputs for forward pass
x1 = torch.randn(5, 4)         # Input tensor with shape [N x M]
inp = torch.randn(4, 3).t()    # Input tensor with shape [M x L] of size 'inp' passed as a keyword argument to the forward function

 