
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.m = torch.nn.Linear(3, 8)
        self.inp = inp
 
    def forward(self, x1, x2):
        v1 = self.m(x1)
        v2 = v1 + self.inp
        return v2


# Initializing the model
m = Model(50)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(2, 8)
