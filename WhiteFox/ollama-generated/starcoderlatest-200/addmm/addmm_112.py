
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.m = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = self.m(x1)
        v2 = torch.mm(v1, v2) + inp
        return v6


# Initializing the model
inp = torch.randn(4, 3, 64, 64)
m = Model(inp)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
