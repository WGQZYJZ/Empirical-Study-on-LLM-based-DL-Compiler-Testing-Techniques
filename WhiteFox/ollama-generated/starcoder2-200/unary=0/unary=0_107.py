
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3  = v1 * v1 # Square the output of the convolution
        v4  = v3 * v1 # Cube the output of the convolution
        v5  = v4 * 0.044715 # Multiply the cube of the output of the convolution by 0.044715
        v6  = v1 + v5 # Add the output of the convolution to the result of the previous operation
        v7  = v6 * 0.7978845608028654 # Multiply the result of the previous operation by 0.7978845608028654
        v8  = torch.tanh(v7) # Apply the hyperbolic tangent function to the result of the previous operation
        v9  = v8 + 1 # Add 1 to the output of the hyperbolic tangent function
        v10 = v2 * v9 # Multiply the output of the convolution by the output of the hyperbolic tangent function

        return v10


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)







