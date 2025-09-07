
class Model(torch.nn.Module):
    def __init__(self, other1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + other1  # Add another tensor to the output of the convolution
        return v2


# Initializing the model and passing an input as a keyword argument