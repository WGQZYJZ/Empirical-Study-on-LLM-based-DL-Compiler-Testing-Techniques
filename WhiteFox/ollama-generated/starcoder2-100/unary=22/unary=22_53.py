
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x2) # Apply pointwise convolution with kernel size 4 to the input tensor
        v3  = torch.tanh(v1) 
        return v3


# Initializing the model