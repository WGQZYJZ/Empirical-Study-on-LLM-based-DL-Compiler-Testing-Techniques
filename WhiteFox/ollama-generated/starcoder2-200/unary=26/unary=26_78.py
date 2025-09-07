
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose1d(3,8,7)
        self.negative_slope  = negative_slope
 
    def forward(self, x):
        v1  = self.convT(x)
        v2  = v1 >0 
        v3  = v1 * self.negative_slope
        v4  = torch.where(v2, v1, v3) # mask the values in v3 with -0.25
        return v4


# Initializing the model
m  = Model(0.25)


# Inputs to the model
x  = torch.randn(64,7)
__output__  = m(x)
