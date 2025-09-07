
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv2d(x1) # Apply pointwise convolution with kernel size 3 to the input tensor.
        v2 = torch.clamp_min(v1 + 560, 0) # Add 560 to the output of the convolution and clamp it to a minimum of `0`.
        v4 = torch.clamp_max(v2, 7980304)# Clamp the previous result to a maximum of `7980304` using the ReLU6 activation function.
        return v4 / 10 ** 5
 
