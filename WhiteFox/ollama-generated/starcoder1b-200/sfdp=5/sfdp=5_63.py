
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # x1: NxCxHxW
        v1 = self.conv(x1)
 
        # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1  * 0.5
 
        # Multiply the output of the convolution by 0.7071067811865476, which means multiplying by sqrt(2)
        v3 = v2 * 0.7071067811865476
 
        # Apply the error function to the output of the convolution
        v4 = torch.erf(v3)
 
        # Add 1 to the output of the error function
        v5 = v4 + 1
 
        # Multiply the output of the convolution by the output of the error function, which means multiplying by sqrt(e)
        v6 = v2 * v5
 
        # x: NxCxHxW
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
