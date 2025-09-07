
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1): 
        v1  = self.conv(x1) # Applying pointwise convolution to input tensor
        v2  = torch.tanh(v1) # Applying hyperbolic tangent activation function on the output of pointwise conv.
        return v2


# Initializing model and its inputs