
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(32, 64, 1)
        self.negative_slope  = negative_slope
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = (v1 > 0).float() # mask
        v3  = v1 * -1.5  # t1 * neg_slope = negative_slope * v1
        v4  = torch.where(v2, v1, v3 )# t2 = torch.where(tmask, t1, t3)
        return v4
 
# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(64, 32, 38, 50)
__output__  = m(x)