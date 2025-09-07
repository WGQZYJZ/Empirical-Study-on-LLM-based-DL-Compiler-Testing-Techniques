
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 8, 4)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float()
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3) 
        return v4

# Initializing the model
m = Model(negative_slope=0.3)

 # Inputs to the model
x1  = torch.randn(65536, 1, 9, 8) 
 __output__  = m(x1)
 