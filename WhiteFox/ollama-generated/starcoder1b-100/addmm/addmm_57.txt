
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.m = torch.nn.Linear(10, 2)

    def forward(self, x1, inp=None):
        v1 = self.m(x1).view(-1, 2)
        v2 = torch.mm(v1, v1.t())
        v3 = torch.mul(inp, v2) # Use keyword argument to be able to set the default value of 'inp'
        return v3


# Initializing the model
m  = Model()


