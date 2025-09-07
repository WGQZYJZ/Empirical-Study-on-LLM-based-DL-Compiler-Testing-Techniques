
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v4  = negative_slope
        v5  = v1 * v4 
        v6  = torch.where(v2, v1, v5)

        return v6

# Initializing the model with a negative slope parameter (default value: 0.25)
m = Model()


# Inputs to the model using the default negative_slope=0.25
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


# Initializing the model with a negative slope parameter (negative_slope=-0.987)
m = Model(-0.987) # Use -0.987 as the negative_slope value instead of default 0.25


# Inputs to the model using the negative_slope parameter (-0.987)
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)