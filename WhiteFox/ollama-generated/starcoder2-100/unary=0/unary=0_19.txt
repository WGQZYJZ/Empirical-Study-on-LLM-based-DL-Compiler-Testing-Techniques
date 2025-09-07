
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3   = v1 * v1 # squared
        v4   = v3 * v1 # cubed
        v5   = v4 * 0.044715 # multiply the cube of the output by a constant 
        v6   = v1 + v5 # add the output to the result of the previous operation, 
        v7   = v6  * 0.7978845608028654 # multiply the result of the previous operation with another constant
        v8   = torch.tanh(v7) # apply hyperbolic tangent to the result of the previous operation, 
        v9   = v8 + 1 # add a constant to the output of the hyperbolic tangent function
        v10  = v2 * v9  # multiply the convolution by another constant 
        return v10


# Initializing model