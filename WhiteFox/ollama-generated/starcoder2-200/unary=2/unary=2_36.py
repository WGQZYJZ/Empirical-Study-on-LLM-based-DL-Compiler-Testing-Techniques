
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5 
        v3  = v1 ** 3 # Cube the transposed convolution output
        v4  = v3 * 0.044715 # Multiply the cubed output by a constant
        v5  = v1 + v4  # Add the transposed convolution to multiplication and addition
        v6  = v5 * 0.7978845608028654 # Multipply the added output by another constant 
        v7  = torch.tanh(v6) # Apply hyperbolic tangent function 
        v8  = v7 + 1 # Add one to the hyperbolic tangent 
        v9  = v2 * v8
        return v9

# Initializing model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

# Output from the previous version of the model. For more information on this, please refer to the initial input.
__prev_output__ = torch.tensor([[-0.89725387-0.5640753 -0.49973217]], dtype=torch.float32)

