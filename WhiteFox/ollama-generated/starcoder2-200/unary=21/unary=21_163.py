
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.tanh(v1) # pass through hyperbolic tangent activation function 
        return v2
# Initializing the model