
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.minv  = kwargs['min']
        self.maxv  = kwargs['max']
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5 * v1, max=3.745618591512478e-07) # clamp_min is used to clamp the output of the convolution to a minimum value. The minimum value here is 0.5 times the maximum value of the output. The maximum value of the output is set by 3.745618591512478e-07
        v3 = torch.clamp_max(v2, max=self.maxv) # clamp_min is used to clamp the output of the convolution to a minimum value. The maximum value here is provided as a keyword argument
        return v3


# Initializing the model
m  = Model()
minv  = -100
maxv  =  50
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

