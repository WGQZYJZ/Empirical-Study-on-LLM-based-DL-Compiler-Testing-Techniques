
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.convTranspose  = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x):
            v1  = self.convTranspose(x)
            v2  = (v1 > 0).float()
            v3  = v1 * negative_slope
            v4  = torch.where(v2 , v1 , v3 )
        return v4


# Initializing the model with a custom negative slope parameter
negative_slope  = 0.5
 
m = Model(negative_slope)

 # Inputs to the model
 x1 = torch.randn(8, 6, 200, 200)
 
 __output__  = m(x1)
