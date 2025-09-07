
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.tanh(v1) # Apply hyperbolic tangent to the output of the transposed convolution
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
__output__  = m(x1)

