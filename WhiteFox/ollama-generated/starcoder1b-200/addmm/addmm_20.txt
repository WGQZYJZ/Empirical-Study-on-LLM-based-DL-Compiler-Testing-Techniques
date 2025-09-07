
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
        self.inp = torch.tensor([0.34567]) # A dummy input tensor

    def forward(self, x1, x2, inp=None):  # The first three arguments are used to feed the model
        v1 = x1  # This is the second argument of 'forward'
        v2 = v1 + inp
        return v2


# Inputs to the model
x1  = torch.randn(1, 4)
inp  = torch.randn(1, 1)
