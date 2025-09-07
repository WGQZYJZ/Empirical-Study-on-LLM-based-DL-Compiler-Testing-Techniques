
class Model(torch.nn.Module):
    def __init__(self, inp = None):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model with an input tensor 'inp' for the 2nd argument of the `forward` function (equivalent to passing it as a keyword argument). The tensor should be passed as a positional argument.
m = Model(torch.randn(1, 8))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
