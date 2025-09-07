
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.conv_transpose2d(x1) # Apply pointwise transposed convolution to the input tensor
        v3  = torch.tanh(v1)  # Apply hyperbolic tangent function to output of the conv transpose op
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(4, 20, 64, 64)
 
__output__  = m(x1)

