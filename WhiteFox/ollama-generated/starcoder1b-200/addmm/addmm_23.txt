
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor):
        super().__init__()
        self.inp = inp

    def forward(self, x1, x2):
        v1 = torch.mm(x1, self.inp) + self.inp
        return v1

# Initializing the model
m = Model(torch.randn((3, 2)))

# Inputs to the model
x1 = torch.randn((1, 3, 64, 64))
x2 = torch.randn((1, 3, 64, 64))
