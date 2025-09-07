
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
 
    def forward(self, x):
        v1 = self.conv(x) 
        v2 = v1 + 3 # Addition
        v3 = torch.clamp_min(v2, 0) # clamp
        v4 = torch.clamp_max(v3, 6)# clamp
        v5 = v4 / 6   # Division by division
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model 
x1 = torch.randn(1, 3, 64, 64) 
 __output__= m(x1)
 
 