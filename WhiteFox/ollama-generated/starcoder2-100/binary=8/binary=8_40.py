
class Model(torch.nn.Module):
    def __init__(self, other=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x): 
        v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + other # Add another tensor "other" to the output of the convolution
        return v2

# Initializing model with an additional parameter and inputs to it