
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to the input tensor
        v2  = v1 * 0.5 # Multiply the output of the linear transformation by 0.5
        v3  = (v1  * v1  * v1 ) + (v1  * v1  * v1 ) 
        v4  = torch.tanh(v3) + 1
        v7 = v2*v4 # Multiply the output of the linear transformation by the output of the hyperbolic tangent function
        return v7

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 3)
__output__  = m(x1)

