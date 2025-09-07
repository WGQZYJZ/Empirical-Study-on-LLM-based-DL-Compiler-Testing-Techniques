
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2a = (v1 > 0).float() * v1
        v4b = torch.where(
            (v1 > 0), 
            v1, 
            -negative_slope*v1 
        )
        return v4b
 
# Initializing the model with a negative slope of 0.25
m = Model(negative_slope=0.25)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)