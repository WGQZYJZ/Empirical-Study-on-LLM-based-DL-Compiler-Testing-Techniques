
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1=None, inp=None):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()
inp_tensor = torch.randn(3, 4)


# Inputs to the model
