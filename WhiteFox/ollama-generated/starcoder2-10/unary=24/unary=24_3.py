
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * 1.0
        v3 = v1 * 0.5
        v4 = torch.where(v2 == True, v1 , negative_slope*v1 + (1 - v2)*v3)
        return v4


# Initializing the model
m = Model(-0.789683279516638)
# Inputs to the model
x1  = torch.randn(1,3, 33,33)
__output__  = m(x1)