
class Model(torch.nn.Module):
    def __init__(self, minv=1000., maxv=2000.):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 / minv # divide the output of the transposed convolution by a minimum value (min_value is provided as keyword argument to __init__())
        v3  = torch.clamp(v2, max=maxv) # clamp the output of the previous operation to a maximum value 
        return v3
# Initializing the model
m1  = Model()
 
# Inputs to the model
x1  = torch.randn(1000, 3, 56, 56)
__output__   = m(x1)

