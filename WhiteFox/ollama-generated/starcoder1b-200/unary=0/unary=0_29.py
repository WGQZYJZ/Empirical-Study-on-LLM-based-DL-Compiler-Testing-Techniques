
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(2).sum(dim=(0, 2, 3), keepdim=True) # Square the input tensor
        v2 = v1.mul(v1).mul(0.044715).tanh()  # Apply the hyperbolic tangent function to the square of the input tensor
        v3 = v2.sum(dim=(0, 2, 3), keepdim=True) * 0.7978845608028654  # Multiply the square of the output of the hyperbolic tangent function by 0.7978845608028654
        v4 = torch.tanh(v3) + 1  # Add 1 to the output of the hyperbolic tangent function
        v5 = v2 * v4  # Multiply the square of the output of the convolution by the output of the hyperbolic tangent function
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
