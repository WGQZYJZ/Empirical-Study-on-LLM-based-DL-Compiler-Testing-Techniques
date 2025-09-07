
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).type_as(torch.zeros(1)) 
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) 
        return v4

# Initializing the model
negative_slope  = 0.5 # A random constant between 0 and 1 used to create a negative slope in the implementation of LeakyReLU
m = Model(negative_slope=negative_slope)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

