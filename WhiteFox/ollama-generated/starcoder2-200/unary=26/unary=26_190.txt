
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,5)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = v1 > 0
        v4  = self.negative_slope * v1
        v6  = torch.where(v2, v1, v4) # the same as: `v3  = (v1 < 0).float() * negative_slope * v1  + ((v1 >= 0).float() * v1)`
        return v6

# Initializing the model
m  = Model(negative_slope=0.1)

 # Inputs to the model
x1 = torch.randn(2,3,48,48)
