
class Model(torch.nn.Module):
    def __init__(self, minval=None, maxval=None):
        super().__init__()
        self.convtrans = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.convtrans(x1)
        v2 = torch.clamp_min(v1, minval=None) # Change the minimum value to a given value and regenerate the model
        v3 = torch.clamp_max(v2, maxval=None)  # Change the maximum value to a given value and regenerate the model
        return v3


# Initializing the model with specified minimum and maximum values
m  = Model(minval=-1, maxval=500)
 
# Inputs to the model
x2  = torch.randn(1, 8, 64, 64)
