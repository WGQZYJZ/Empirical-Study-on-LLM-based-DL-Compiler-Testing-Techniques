
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp=None, x1=None, x2=None):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4, 5, 6)
x2 = torch.randn(7, 8, 9, 10)
inp = torch.randn(6, 3) # An additional input tensor
