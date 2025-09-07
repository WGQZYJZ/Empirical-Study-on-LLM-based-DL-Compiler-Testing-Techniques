
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.clamp_min(v1, -50) # Clamp the output of the previous operation to a minimum value
        v3 = torch.clamp_max(v2, +50)  # Clamp the output of the previous operation to a maximum value
        return v3

# Initializing the model
m = Model()


# Inputs to the model