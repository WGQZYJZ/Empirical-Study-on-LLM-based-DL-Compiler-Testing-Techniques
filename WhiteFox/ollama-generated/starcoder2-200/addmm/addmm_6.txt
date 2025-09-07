
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x2)  # Matrix multiplication on two input tensors
        v2 = v1 + self.inp_tensor() if inp is None else inp  # Add the result of the matrix multiplication to another tensor 'inp'
        return v2
 
    def inp_tensor(self):
        return torch.randn(64, 3)
 
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 3)
