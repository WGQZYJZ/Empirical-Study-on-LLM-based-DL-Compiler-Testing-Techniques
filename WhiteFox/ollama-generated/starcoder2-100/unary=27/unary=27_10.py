
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor.
        v2  = torch.clamp_min(v1, min=-30.) # Clamp the output of the previous operation to a minimum value.
        v3  = torch.clamp_max(v2, max=+30) # Clamp the result of the previous operation to a maximum value.
        return v3
