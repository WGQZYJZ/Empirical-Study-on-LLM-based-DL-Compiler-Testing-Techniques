
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x2)  # input tensors have different shapes in this pattern.
        v3 = v1 + inp
        return v3


# Initializing the model
m = Model()


# Inputs to the model
__output__, t1  = m(input1=t1, inp=inp), t2

