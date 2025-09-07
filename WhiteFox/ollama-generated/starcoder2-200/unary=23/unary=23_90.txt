
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = convT(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the transposed convolution
        return v2


# Initializing model
m = Model()
 

# Inputs to the model
x1 = torch.randn(3, 8, 40, 70)
 
