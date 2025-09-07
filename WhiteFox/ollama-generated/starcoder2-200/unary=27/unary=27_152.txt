
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1.clamp_min_(0)  
        v3  = v2.clamp_max_(255) # clamp the result of the previous operation to a maximum value   
        return v3
 
# Initializing the model  
m  = Model()
 
 
# Inputs to the model: 
x1  = torch.randn(1, 3, 64, 64)  
 