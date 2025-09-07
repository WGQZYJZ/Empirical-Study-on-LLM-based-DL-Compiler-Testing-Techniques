
class Model(torch.nn.Module):
    def __init__(self, minval=-10., maxval=24):
        super().__init__()
        self.linear = torch.nn.Linear(3*64**2, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, -10.)
        v3  = torch.clamp_max(v2, 24.)
        return v3


# Initializing the model
m  = Model()
 
 
 # Inputs to the model 
 x1  = torch.randn(6, 3*64**2)

 # Model outputs from model
  __output__  = m(x1)
