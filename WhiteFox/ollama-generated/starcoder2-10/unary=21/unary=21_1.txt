
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self._a_normal()  # Normal
        v2 = torch.tanh(v1)  # Hyperbolic tangent activation function
        return v2
 
 
class _a_normal:
    def __call__(self):
        v3 = torch.rand(4, 5) 
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


