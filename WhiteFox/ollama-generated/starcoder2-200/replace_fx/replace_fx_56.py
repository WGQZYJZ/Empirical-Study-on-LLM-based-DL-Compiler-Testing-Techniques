
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1, 3) # Replace with rand_like
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(50, 480).double()
__output__  = m(x1)
