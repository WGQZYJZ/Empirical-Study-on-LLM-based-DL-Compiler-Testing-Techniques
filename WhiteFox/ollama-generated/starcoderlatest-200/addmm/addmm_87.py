
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp=None):
        if inp is not None:
            self.inp = inp
        t1 = torch.mm(x1, self.inp)
        v2 = t1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(8)
