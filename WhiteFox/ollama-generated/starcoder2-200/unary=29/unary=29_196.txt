
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply a pointwise transposed convolution to the input tensor
        v2 = torch.clamp_min(v1, -90) # Clamp the output of the previous operation to a minimum value -90
        v3 = torch.clamp_max(v2, 54) # Clamp the output of the previous operation to a maximum value 54
        return v3


# Initializing model with minimum and maximum values provided as keyword arguments.
m = Model()
min_value, max_value = -109, 78
__output__  = m(x)

