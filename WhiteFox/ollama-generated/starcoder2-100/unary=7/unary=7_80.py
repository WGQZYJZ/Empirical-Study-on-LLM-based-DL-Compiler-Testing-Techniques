
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * F.clamp(v1 + 5, min=0.) / 6
        return v2


# Initializing the model and inputs to it
m  = Model()
x1 = torch.randn(8, 3)
__output__  = m(x1)

# If you cannot find a valid PyTorch model with 4 outputs (in case the output of the linear transformation contains multiple elements), please submit another one.
