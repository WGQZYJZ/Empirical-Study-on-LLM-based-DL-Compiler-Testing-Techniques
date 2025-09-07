
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(2)
        return [
            self._linear(v0),  # Apply a linear transformation to the input vector v0
            self._tanh(self._linear(v0))  # Apply the hyperbolic tangent function to the output of the linear transformation, where 'self' is defined as the parent class in torch.nn.Module
        ]
 
    def _linear(self, x):
        return x @ torch.randn((x.size(-1), ))
    
    def _tanh(self, y):
        return torch.tanh(y)


# Initializing model
m = Model()
 
__output__  = m(torch.rand(2))

