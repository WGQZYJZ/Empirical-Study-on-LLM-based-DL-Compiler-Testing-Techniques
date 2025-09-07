
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1=None, x2=None, inp=0):  # Two positional and one named arguments required to be provided
        v1 = torch.mm(x1, x2) + inp 
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3840, 675)
x2  = torch.randn(3840, 675)
inp = 0
__output__  = m(x1=x1, x2=x2, inp=inp)

