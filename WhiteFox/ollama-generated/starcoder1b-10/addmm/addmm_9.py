
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp = torch.randn(10, 2)

    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()


