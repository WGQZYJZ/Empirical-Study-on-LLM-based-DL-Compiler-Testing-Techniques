
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + self.other  # Add another tensor `other` to the output of the convolution
        return v2

# Initializing the model
m = Model(torch.randn(3,8,4))

