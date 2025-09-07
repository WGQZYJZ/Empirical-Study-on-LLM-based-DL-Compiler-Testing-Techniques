
class Model(torch.nn.Module):
    def __init__(self, inp=1):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v1 + self.inp


# Initializing the model
m = Model()
# Keyword arguments are set here:
m.inp = 5
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
