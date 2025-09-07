
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
         v1  = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
         v2  = torch.clamp_min(v1, min=0.5) # Clamp the output of the convolution to a minimum value of 0.5
         v3  = torch.clamp_max(v2, max=6.4) # Clamp the output of the previous operation to a maximum value of 6.4
        return v1

# Initializing the model