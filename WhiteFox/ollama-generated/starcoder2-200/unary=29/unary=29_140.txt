
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v01  = self.convt(x1)  # Apply pointwise transposed convolution to the input tensor
        v02 = torch.clamp_min(v01, min=0.5) # Clamp the output of the transposed convolution to a minimum value of `0.5`
        return torch.clamp_max(v02, max=3.0)  # Clamp the output of the previous operation to a maximum value of `3.0`


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

