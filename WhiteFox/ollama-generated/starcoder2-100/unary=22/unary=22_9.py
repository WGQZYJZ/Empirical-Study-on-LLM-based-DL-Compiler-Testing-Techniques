
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying a linear transformation to the input tensor
        v2  = torch.tanh(v1) # Applying hyperbolic tangent function on the output of the linear transformation 
        return v2


# Initializing model
m  = Model() 


# Inputs to the model
x1  = torch.randn(5, 32)
__output__  = m(x1)
