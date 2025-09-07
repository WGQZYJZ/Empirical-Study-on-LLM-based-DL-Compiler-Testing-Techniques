
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x2) # Perform matrix multiplication on two input tensors
        if not inp:
            v2  = v1 
        else : 
            v2  = v1 + inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v2

# Initializing the model
m = Model()


# Inputs to the model
inp=torch.rand(4,5)
inp=torch.randn(4,5)
x1= torch.rand(300, 6789)# Tensor of shape [N x P]
x2 = None
