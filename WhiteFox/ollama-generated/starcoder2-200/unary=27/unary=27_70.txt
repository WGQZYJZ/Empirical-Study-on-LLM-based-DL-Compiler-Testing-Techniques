
class Model(torch.nn.Module):
    def __init__(self, minValue=0., maxValue=-1e9):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  + minValue - torch.min(v1) 
        v3  = torch.clamp_max(v2, maxValue=maxValue) 
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)