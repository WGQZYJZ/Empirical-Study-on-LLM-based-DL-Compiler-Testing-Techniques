
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(32, 64)
        self.m2 = torch.nn.Linear(64, 32)
 
    def forward(self, x1, inp=1.0):
        v1 = torch.mm(x1, x1)
        v2 = torch.mm(v1, x1) + inp
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 16)
inp = torch.randn(64, 32)
