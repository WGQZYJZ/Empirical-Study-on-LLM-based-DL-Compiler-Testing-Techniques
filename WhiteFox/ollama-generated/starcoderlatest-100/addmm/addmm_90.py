
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=torch.ones((64, 1, 32, 64))):
        v1 = torch.mm(x1, inp)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 32, 64)
inp = torch.randn(1, 1, 64, 64)
