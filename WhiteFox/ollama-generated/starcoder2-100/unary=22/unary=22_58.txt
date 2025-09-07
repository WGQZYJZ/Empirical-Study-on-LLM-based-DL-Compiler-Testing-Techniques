
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.sum(x1)  # Sum the elements of the input tensor
        v2 = torch.tanh(v1 + 3)  # Add a constant to each element and then apply the hyperbolic tangent function to the sum
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8, 64)
__output__  = m(x1)
