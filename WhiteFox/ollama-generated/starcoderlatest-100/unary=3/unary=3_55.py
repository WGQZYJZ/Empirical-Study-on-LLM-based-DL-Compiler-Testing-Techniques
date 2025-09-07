
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 4, 3, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5 # Apply pointwise convolution with kernel size 3 to the input tensor
        v2 = v1 * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
        v3 = torch.erf(v2) + 1 # Apply the error function to the output of the convolution, and then add 1 to the output of the error function
        v4 = v3 * v2  # Multiply the output of the convolution by the output of the error function
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 1, 64, 64)
