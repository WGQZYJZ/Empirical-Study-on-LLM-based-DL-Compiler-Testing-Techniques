
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        v1  = self.linear(x) # Applying a linear transformation to the input tensor
        v2  = torch.tanh(v1)# Applying the hyperbolic tangent function to the output of the linear transformation 
        return v2

# Initializing and running model on inputs
m  = Model()
__output__  = m(x)

