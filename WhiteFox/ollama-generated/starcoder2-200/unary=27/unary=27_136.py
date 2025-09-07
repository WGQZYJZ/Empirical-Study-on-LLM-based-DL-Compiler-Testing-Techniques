
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.clamp_min(v1, -0.5) # Clamp the output of the convolution to a minimum value (-0.5 here)
        v3  = torch.clamp_max(v2, 64.) # Clamp the output of the previous operation to a maximum value (64 here)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
