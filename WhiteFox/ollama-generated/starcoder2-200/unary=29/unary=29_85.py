
class Model(torch.nn.Module):
    def __init__(self, maxv=400., minv=-275.)
        super().__init__() 
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x):
        v1  = self.convt(x) # Apply pointwise transposed convolution to the input tensor
        v2  = torch.clamp_min(v1, minv) # Clamp the output of the transposed convolution to a minimum value `minv` 
        return torch.clamp_max(v2, maxv) # Clamp the output of the previous operation to a maximum value `maxv`

# Initializing model
m = Model()

# Input for model
x  = torch.randn(1, 3, 64, 64)

