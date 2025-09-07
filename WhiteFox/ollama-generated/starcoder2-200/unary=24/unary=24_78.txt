
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = (v1 > 0).float() # This creates the mask from the output of conv
        v3  = v1 * (-self.negative_slope)
        v4  = torch.where(v2, v1, v3)
        return v4

m = Model()

 x1  = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)
