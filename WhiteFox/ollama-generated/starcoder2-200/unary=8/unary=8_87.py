
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.convT(x1) # Applying pointwise transposed convolution to the input tensor 
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0)
        v4  = torch.clamp(v3, max=6)
        v5  = v1 * v4  # Applying multiplication operation on transposed convolution's output and clamped tensor
        v6  = v5 / 6  
        return v6


# Initializing the model
m  = Model()
 
# Inputs to the model
x2  = torch.randn(3,10,8) 
 
__output__  = m(x2)