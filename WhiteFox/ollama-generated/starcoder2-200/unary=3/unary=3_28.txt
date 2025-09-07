
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1) * 0.5 # Apply pointwise convolution with kernel size 1 to the input tensor and multiply by 0.5
        v2 = v1 + 0.7071067811865476  # Add 0.7071067811865476 to the output of the pointwise convolution
        v3 = torch.erf(v2)  # Apply error function on the result
        v4  = self.conv(x3) * v3 + 1   # Multiply the output by another constant, add 1 and then multiply that result by another constant to get the output
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

