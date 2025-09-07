
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None, y1=None, x2=None, y2=None):
        v1 = torch.mm(x1[0], x2[0]) # Perform matrix multiplication on two input tensors
        v2  = v1 + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m  = Model()


# Inputs to the model