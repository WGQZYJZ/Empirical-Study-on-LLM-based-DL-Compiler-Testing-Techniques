
class Model(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()
        self.linear  = torch.nn.Linear(dim, dim)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply the linear transformation to the input tensor
        v2  = torch.tanh(v1)  # Apply the hyperbolic tangent function to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64*64)

__output__  = m(x1)