
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.inp = torch.tensor(inp)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2 = v1 + self.inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 64, 64)
x2 = torch.randn(4, 4)
