
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 1)
 
    def forward(self, x):
        v0  = torch.nn.functional.linear(x, self.linear) # Apply a linear transformation to the input tensor using PyTorch's functional API
        v1  = torch.tanh(v0) # Apply the hyperbolic tangent function to the output of the linear transformation (the result from the previous line of code in PyTorch)
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(32, 32)
__output__  = m(x)

