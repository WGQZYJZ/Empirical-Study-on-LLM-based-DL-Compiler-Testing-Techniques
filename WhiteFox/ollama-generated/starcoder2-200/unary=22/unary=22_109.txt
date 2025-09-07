
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
 
    def forward(self,  x1):
        v1 = torch.nn.Linear(3, )
        v2 = v1(x1) # Apply a linear transformation to the input tensor
        v3 = torch.tanh(v2) # Apply the hyperbolic tangent function to the output of the linear transformation
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
__output__  = m(x1)

