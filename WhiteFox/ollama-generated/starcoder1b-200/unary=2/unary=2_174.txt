
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 3 * 64 * 64)
        v2 = v1 * 0.5
        v3 = v1 ** 3  # Powers the output of the convolution by `2**3` to create a cube
        v4 = v3 * 0.044715  # Multiply the cubed output by 0.044715
        v5 = v1 + v4  # Add the output of the convolution to the output of the multiplication
        v6 = v5 ** 2 * 0.7978845608028654  # Multiply the output of the addition by 0.7978845608028654
        v7 = torch.tanh(v6)  # Apply the hyperbolic tangent function to the output of the multiplication
        v8 = v7 + 1  # Add 1 to the output of the hyperbolic tangent function
        v9 = v2 * v8  # Multiply the output of the multiplication by the output of the addition
        return v9


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
