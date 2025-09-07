
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.neg_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float()
        v2 = torch.where(mask, v1, -1 * self.neg_slope * v1) 
        return v2


# Initializing the model
m = Model(-0.3) 


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) 
__output__  = m(x1)
 
