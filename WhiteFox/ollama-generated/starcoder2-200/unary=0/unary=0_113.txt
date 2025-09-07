
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3 = v1 ** 3 # Cube the output of the convolution
        v4 = v3 * 0.044715 # Multiply the cube of the output of the convolution by 0.044715
        v5 = v1 + v4 # Add the output of the convolution to the result of the previous operation 
        v6 = v5 * 0.7978845608028654 # Multiply the result of the previous operation by 0.7978845608028654
        v7 = torch.tanh(v6) # Apply the hyperbolic tangent function to the result of the previous operation 
        v8 = v7 + 1 # Add 1 to the output of the hyperbolic tangent function 
        v9 = v2 * v8 # Multiply the output of the convolution by the output of the hyperbolic tangent function
        return v9


# Initializing the model