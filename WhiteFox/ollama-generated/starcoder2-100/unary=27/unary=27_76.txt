
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = v1.clamp_min(-5000.)
        v3  = v2.clamp_max(+5000.)
        return v3

# Initializing the model and setting the minimum/maximum value 
m = Model()
m.conv._parameters['weight'].data[...]

 # Inputs to the model 
x1  = torch.randn(1, 3, 64, 64) 
 