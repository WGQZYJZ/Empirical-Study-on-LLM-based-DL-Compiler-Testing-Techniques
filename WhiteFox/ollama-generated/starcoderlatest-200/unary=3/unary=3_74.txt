
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5 # Multiply the output of the convolution by 0.5
        v2 = self.conv(x1) * 0.7071067811865476 # Multiply the output of the convolution by 0.7071067811865476
        v3 = torch.erf(v2) # Apply the error function to the output of the convolution
        v4 = self.conv(x1) + 1 # Add 1 to the output of the error function
        v5 = v1 * v3 # Multiply the output of the convolution by the output of the error function
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
