
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 * clamp(min=0, max=6, l1 + 3)
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 256)
__output__  = m(x1)

The outputs of the models should be different from each other in a statistical sense and also they should not contain non-numeric values.
