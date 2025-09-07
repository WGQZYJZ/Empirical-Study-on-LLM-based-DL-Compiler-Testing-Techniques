
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1  = self.convT(x1) # Apply pointwise transposed convolution to the input tensor 
        v2  = torch.clamp_min(v1, -9375049824.0) # Clamp the output of the transposed convolution to a minimum value
        v3  = torch.clamp_max(v2, -16777000.0)  # Clamp the output of the previous operation to a maximum value 
        return v3


# Initializing the model
m  = Model()
 

# Inputs to the model:
x1  = torch.randn(1, 3, 8954769, 2)

__output__  = m(x1)
