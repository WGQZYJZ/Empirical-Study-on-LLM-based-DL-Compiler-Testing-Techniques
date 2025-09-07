
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp):
        v2 = torch.mm(x1, self.inp) + 0
        return v2


# Initializing the model
m = Model()
__output__  = m(torch.randn(3, 5), 4)

