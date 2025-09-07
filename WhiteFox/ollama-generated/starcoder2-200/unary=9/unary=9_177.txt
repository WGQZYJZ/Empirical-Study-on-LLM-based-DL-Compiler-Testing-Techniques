
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3 # Apply pointwise convolution with kernel size 1 to the input tensor and add 3 to the output of the convolution.
        v2 = torch.clamp_min(v1, 0) # Clamp the result from the previous step by clamping it to a minimum value of zero (which will be used as the ReLU6 activation function).
        v3 = torch.clamp_max(v2, 6) # Clamp the previous output of the addition operation to ensure that it is not greater than 6.
        v4 = v3 / 6 # Divide the clamped output by six (to get a normalized value that can be used as an input for other neural network operations).
        return v4


# Initializing the model and generating inputs:
m1= Model()
x1  = torch.randn(5, 32)
 
