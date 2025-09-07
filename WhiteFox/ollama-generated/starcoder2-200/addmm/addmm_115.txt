
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp=None):
        t0 = torch.mm(x1, inp) # matrix multiplication operation performed on two input tensors
        t1 = t0 + 2 * inp  # add a tensor to the result of the matrix multiplication 
        return t1


# Initializing the model
m = Model()
 
# Inputs to the model with keyword argument
x1 = torch.randn(3,4)
inp = torch.randn(3,4)
__output__  = m(x1, inp=inp)