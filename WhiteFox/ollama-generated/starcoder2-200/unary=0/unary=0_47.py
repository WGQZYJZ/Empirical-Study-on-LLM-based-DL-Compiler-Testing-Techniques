
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 ** 3 # Square the output of the convolution
        v4  = v3 * 0.044715 
        v6  = v1 + v4 # Add the output of the convolution to the result of the previous operation
        v8  = torch.tanh(v6) 
        v9  = v8 + 1
        v12 = v2 * v9 # Multiply the output of the convolution by the output of the hyperbolic tangent function
        return v12


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
