
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * 0.5      # Multiply the output of the convolution by 0.5
        v3  = v2 ** 3       # Square the output of the convolution and then multiply it by the output of the previous operation
        v4  = v3 + 0.7978845608028654 * v1  # Add to the result of the previous operation the output of the convolution multiplied by a constant 0.7978845608028654
        v5  = torch.tanh(v4) + 1   # Apply the hyperbolic tangent function to the result of the previous operation, and then add 1 to it
        v6  = v2 * v5    # Multiply the output of the convolution by the output of the hyperbolic tangent function
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
