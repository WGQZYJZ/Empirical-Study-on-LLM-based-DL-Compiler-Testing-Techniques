
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 5, stride=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.25
        v3 = v1 * v1 # Cube the output of the convolution
        v4 = v3 * v1 # Tenthecube of the output of the convolution
        v5 = v4 * 0.08943
        v6 = v1 + v5
        v7 = v6 * 0.202116
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9 # Multiply the output of the convolution by the output of the hyperbolic tangent function
        return v10


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
