
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3  = v2 ** 3 # Square the result of the previous operation, cubing it again
        v4  = v3 * 0.7978845608028654 # Multiply the cube of the output of the convolution by another constant, 0.7978845608028654
        v5  = v1 + v4 # Add the output of the convolution to the result of the previous operation
        v6  = v5 * torch.tanh(v2) # Multiply the result of the previous operation by another constant, -0.9370297837205873
        v7  = t1 + 0.47140452079668875 # Add another constant to the output of the hyperbolic tangent function, -0.47140452079668875 
        v8  = v6 * t7  # Multiply the result of the previous operation by 0.47140452079668875
        return v8

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

