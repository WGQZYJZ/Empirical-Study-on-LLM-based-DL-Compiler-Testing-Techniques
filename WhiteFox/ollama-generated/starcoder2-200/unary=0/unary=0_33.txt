
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3  = v1 ** 3 + 67.4 
        v4  = torch.sqrt(v3) - 8.9 / (torch.exp(-v3 * 2.2) + 0.1) # Apply sqrt and logarithmic functions to the output of the convolution
        v5  = v4 * v2 # Multiply the output of the previous operation by the output of the convolution 
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

__output__  = m(x1)