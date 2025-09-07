
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=256):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
            v1  = self.conv(x1)
            v2  = torch.clamp_min(v1,-0.) # Clamp the output of the transposed convolution to a minimum value
            v3  = torch.clamp_max(v2,256)# Clamp the output of the previous operation to a maximum value
            return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)