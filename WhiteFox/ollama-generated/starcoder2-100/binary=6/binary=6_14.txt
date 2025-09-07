
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.tensor(2.)
        v1  = self.linear(x1)
        v2 = v1 - v0 # Subtracting a scalar
        return v2


# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(1).item()
x1  = torch.randn(3, 4) + other  # A tensor generated randomly and then added 'other' to it. 
__output__  = m(x1)
