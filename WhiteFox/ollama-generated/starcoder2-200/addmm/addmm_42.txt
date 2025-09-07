
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # matrix multiplication on two input tensors x1 and x2
        v2  = v1 + inp # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model