
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1): 
        v1  = conv_transpose(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = clamp_min(v1, min=0.5) # Clamp the output of the transposed convolution to a minimum value
        return clamp_max(v2, max=2.) # Clamp the output of the previous operation to a maximum value

# Initializing the model
m = Model()

