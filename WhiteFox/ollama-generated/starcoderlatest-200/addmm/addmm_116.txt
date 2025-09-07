
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x1)
        v2 = v1 + inp
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 4, 5)
x2 = torch.randn(2, 3, 4, 5)
inp = torch.randn(2, 1, 4, 5)
