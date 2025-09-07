
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()
m = nn.Sequential(*[m] + [m]) # add another copy of the module

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

