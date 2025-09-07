
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, minValue) # clamped minimum value is provided as a keyword argument of the method
        v3  = torch.clamp_max(v2, maxValue)# clamped maximum value is provided as a keyword argument of the method
        return v3

# Initializing model
m = Model()
 
# Inputs to the model
x1   = torch.randn(1, 3, 64, 64)
