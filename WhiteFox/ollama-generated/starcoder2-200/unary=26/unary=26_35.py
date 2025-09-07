
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask  = v1 > 0 
        v4 = negative_slope * v1 
        v5 = torch.where(mask,v1,v4 )
        return v5

# Initializing the model with negative slope `0.5`
m2 = Model()


# Inputs to the model for the first time
x1  = torch.randn(1,3,64,64)
__output_for_first_time__ = m2(x1)

# Inputs to the model after `2` runs of the forward pass with different negative slope
x2 = torch.randn(1,3,64,64)
