
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v = torch.mm(x1, inp)
        return v + inp


# Initializing the model
m = Model()


# Inputs to the model
inp  = torch.randn(1, 4, 8, 8)
