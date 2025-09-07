
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.rand_like(x1) # A random tensor of the same size as input tensor filled with random numbers.
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 4)
__output__  = m(x1)