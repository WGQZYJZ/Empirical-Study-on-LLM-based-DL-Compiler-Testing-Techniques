
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.conv_transpose(v1, 0.5, (1, 64, 64))
        v3 = v2  * v2  * v2  # Cube the output of the transposed convolution
        v4 = v3  * 0.044715
        v5 = v1 + v4  # Add the output of the transposed convolution to the output of the multiplication
        v6 = torch.nn.functional.tanh(v5)  # Apply the hyperbolic tangent function to the output of the multiplication
        v7 = v6  + 1  # Add 1 to the output of the hyperbolic tangent function
        v8 = v2  * v7  # Multiply the output of the multiplication by the output of the addition
        return v8


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
