
class Model(torch.nn.Module):
    def __init__(self, maxval=500., minval=-300):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 16, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2a = torch.clamp_min(v1, minval=-300) # Clamp the output of the transposed convolution to a minimum value
        v2b = torch.clamp_max(v2a, maxval=500.)  # Clamp the output of the previous operation to a maximum value
        return v2b


# Initializing the model
m  = Model()
 

# Inputs to the model
x1 = torch.randn(16, 8, 32, 32) 

__output__  = m(x1)
