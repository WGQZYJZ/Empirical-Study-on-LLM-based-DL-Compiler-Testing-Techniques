
class Model(torch.nn.Module):
    def __init__(self, inp=1):
        super().__init__()
        self.inp = inp
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Perform matrix multiplication on two input tensors
        v2 = v1 + self.inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m = Model()
