
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0 # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) 
        return v4

# Initializing the model
m  = Model(.7)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
__output__  = m(x1)

