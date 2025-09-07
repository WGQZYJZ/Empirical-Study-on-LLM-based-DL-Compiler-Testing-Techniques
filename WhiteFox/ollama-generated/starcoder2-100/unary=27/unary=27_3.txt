
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.min_value = min_value 
        self.max_value = max_value 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1.clamp_min(self.min_value)
        v3 = v2.clamp_max(self.max_value)
        
        return v3
        
# Initializing the model with provided values for the minimum and maximum values 
m  = Model(-0.5,0.5)

 # Inputs to the model
x1 = torch.randn(1, 3,64,64)
__output__  = m(x1)

