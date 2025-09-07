
class Model(torch.nn.Module):
    def __init__(self, min=1e-320 , max = 1) :
        super().__init__()
        self.conv = torch.nn.Conv2d(3,8, 1,stride=1,padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v4 = torch.clamp_max(v1, max) 
        v5 = torch.clamp_min(v4 , min)    
        return v5

# Initializing the model with minimum value set to 0 and maximum value set to 260.
m=Model(0,260 )

 # Inputs for the model. 
 x1 = torch.randn(1,3,80,80)

 