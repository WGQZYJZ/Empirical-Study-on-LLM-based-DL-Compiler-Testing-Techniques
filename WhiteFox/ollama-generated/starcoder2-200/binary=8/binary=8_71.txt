
class Model(torch.nn.Module):
    def __init__(self, k1 = -2., k2 = 5.43):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.param_1  = k1
        self.param_2  = k2
    
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.param_1 
        v3  = v2 + self.param_2  
        return v3

# Initializing the model with keyword arguments passed to Conv2d constructor
m  = Model(k1=-0.9, k2=5.)

 # Inputs to the model 
x1 = torch.randn(1, 3, 64, 64) 
