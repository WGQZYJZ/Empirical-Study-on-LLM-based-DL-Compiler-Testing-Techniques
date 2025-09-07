

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        return v1 + 5


# Initializing the model and setting `inp` to a non-random tensor value (default is 0s).
m  = Model()
__output__= m(torch.rand((32, 64)), torch.zeros((32, 64)))

