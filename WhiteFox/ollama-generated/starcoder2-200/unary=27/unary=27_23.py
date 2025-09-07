

class Model(torch.nn.Module):
    def __init__(self, min1=None, max2=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2 = torch.clamp_min(v1, min1) # Clamp the output of the convolution to a minimum value
        v3  = torch.clamp_max(v2, max2)# Clamp the output of the previous operation to a maximum value
        return v3

# Initializing the model
m  = Model(min1=0., max2=-4.) # Provide the minimum and maximum values for clamping

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
