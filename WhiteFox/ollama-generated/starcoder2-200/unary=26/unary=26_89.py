
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() * (-self.negative_slope + torch.sqrt(torch.square(-self.negative_slope) * 2 + torch.square(v1)))
        v3  = v1 - v2 
        return v3


# Initializing the model and setting its hyperparameters
m = Model() # negative slope of 0.5 in convtranspose
__output__  = m(x1)