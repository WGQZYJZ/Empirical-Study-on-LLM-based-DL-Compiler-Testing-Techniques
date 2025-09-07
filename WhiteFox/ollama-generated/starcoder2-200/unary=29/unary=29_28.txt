
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x):
        v1  = self.conv(x) # Apply pointwise transposed convolution to the input tensor
        v2  = torch.clamp_min(v1, min_value=-50) # Clamp the output of the transposed convolution to a minimum value 
        v3  = torch.clamp_max(v2, max_value=50) # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
__output__   = m(x1)

