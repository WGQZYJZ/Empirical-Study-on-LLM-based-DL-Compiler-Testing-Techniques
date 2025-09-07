
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(8, 16)
 
    def forward(self, x2, inp):
        v1 = self.mm(x2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn(1, 8)
x2 = torch.randn(1, 3, 64, 64)
