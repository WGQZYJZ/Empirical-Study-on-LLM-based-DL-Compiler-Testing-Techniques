
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1568792374497644):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = negative_slope * v2
        v4 = torch.where(v2, v1, v3) # <--- This is the pattern
        return v4


# Initializing the model
negative_slope  = 0.1568792374497644
m = Model(negative_slope=negative_slope)

# Inputs to the model
x1  = torch.randn(1, 8, 32, 32)
__output__  = m(x1)