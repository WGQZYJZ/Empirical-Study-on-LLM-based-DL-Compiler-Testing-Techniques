
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        if inp:
            t1 = torch.mm(x1, inp)  # Perform matrix multiplication on two input tensors
            t2 = t1 + inp  # Add the result of the matrix multiplication to another tensor 'inp'
        else:
            t1 = None
            t2 = None

        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
