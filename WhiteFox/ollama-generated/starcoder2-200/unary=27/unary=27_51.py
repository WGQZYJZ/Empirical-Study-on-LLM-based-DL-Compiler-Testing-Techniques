
class Model(torch.nn.Module):
    def __init__(self, minv=0., maxv=255):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, minv) # Clamp the output of the convolution to a minimum value (default: 0.)
        v3  = torch.clamp_max(v2, maxv) # Clamp the output of the previous operation to a maximum value (default: 255.).
        return v3


# Initializing the model
m1 = Model()
m2 = Model(-0.794861, 50.)
m3 = Model(maxv=5., minv=-1e-0) # This syntax is correct but the result won't match the previous result because the minimum value in m2 is changed to -1e-0.


# Inputs to the model for the first model (default values of 0 and 255 are used here):
x1 = torch.randn(1, 3, 64, 64)

# Model outputs:
__output__m1  = m1(x1) # torch.Size([1, 8, 64, 64])
__output__m2  = m2(x1) # torch.Size([1, 50, 64, 64])


# Inputs to the model for the third model:
m3  = Model(maxv=5., minv=-1e-0) 

x2 = torch.randint(-79, 80, (1, 3, 64, 64)) # A random input with values from -79 to 80.
m3_output  = m3(x2)

