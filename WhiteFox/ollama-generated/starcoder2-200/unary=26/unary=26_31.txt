
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.convT(x1)
        mask = (v1 > 0).float()
        v2  = torch.where(mask, v1, -v1 * self.negative_slope) 
        return v2


# Initializing the model
m = Model(0.5)
 
# Inputs to the model
x1 = torch.randn(3, 3, 64, 64) 
 
__output__  = m(x1)

