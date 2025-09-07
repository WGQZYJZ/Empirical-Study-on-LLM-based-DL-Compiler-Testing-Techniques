
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 *  0.5 
        v3  = (v1 * v1).pow_(3.)  # Square the output of the convolution, and then cube it
        v4  = v3 *  0.044715    # Multiply the previous operation by another constant 0.044715
        v5  = v2 + (v4)     # Add the output of the convolution to the result of the previous operation 
        v6  = v5 * 0.7978845608028654   # Multiply the output of the previous operation by another constant
        v7  = torch.tanh(v6) # Apply the hyperbolic tangent function to the result of the previous operation
        v8  = v7 +1    # Add one to the output of the hyperbolic tangent function 
        return (v2 * v8 )   