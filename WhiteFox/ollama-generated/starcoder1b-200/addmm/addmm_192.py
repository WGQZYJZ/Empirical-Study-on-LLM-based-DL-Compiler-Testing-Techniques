
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(10, 5)
 
    def forward(self, x1, inp):
        v2  = torch.mm(x1, inp) + inp
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
inp = torch.randn(5, 5)
