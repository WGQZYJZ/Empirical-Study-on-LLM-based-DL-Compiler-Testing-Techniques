
class Model(torch.nn.Module):
    def __init__(self, minval=None, maxval=None):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
        # Setting the minimum and maximum values of clamp operation
        self.minval = minval or -0.954 
        self.maxval = maxval or 0.6
 
    def forward(self, x):
        v1  = self.conv(x)
        v2 = torch.clamp_min(v1, self.minval)
        v3 = torch.clamp_max(v2, self.maxval)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
 
# Running the model
