
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose1d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = (v1 > 0).type_as(v1)
        v3 = v1 * negative_slope 
        v4 = torch.where(v2, v1, v3)   
        return v4

# Initializing the model with a specific negative slope
m  = Model(negative_slope=0.5)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 1) # Generate an input tensor
__output__  = m(x1)

