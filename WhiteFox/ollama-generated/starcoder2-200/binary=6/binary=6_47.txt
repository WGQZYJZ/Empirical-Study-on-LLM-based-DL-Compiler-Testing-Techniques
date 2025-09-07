
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + other # Add 'other' to the output of the convolution
        return v2


# Initializing the model