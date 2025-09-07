
class Model(torch.nn.Module):
    def __init__(self, min_=0., max_=128.):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 4, 3)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, min_=0.) # Clamp the output of the transposed convolution to a minimum value
        v3  = torch.clamp_max(v2, max_=128.) # Clamp the output of the previous operation to a maximum value
 
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(10, 4, 56, 56)

__output__  = m(x)