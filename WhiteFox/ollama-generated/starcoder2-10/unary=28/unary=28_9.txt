
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, 0.) # minimum value 0 is a keyword argument provided in the constructor
        v3 = torch.clamp_max(v2, 64.) # maximum value 64 is a keyword argument provided in the constructor 
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(10, 8)
 
__output__  = m(x1)

