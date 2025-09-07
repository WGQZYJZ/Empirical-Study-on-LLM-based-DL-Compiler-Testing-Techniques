
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        return torch.clamp_min(v1, min), torch.clamp_max(v2, max)


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
min  = -float('inf') # A minimum value to clamp the output of the convolution to
max  = float('inf')  # A maximum value to clamp the output of the convolution to

 