
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(3*49,8)
    
    def forward(self, x1):
      v1 =  self.conv(x1)
      v2 =  torch.clamp_min(v1,-70) # min_value=-70 is provided as a keyword argument to the torch.clamp_min() function 
      v3 = torch.clamp_max(v2,84)# max_value=84 is provided as a keyword argument to the torch.clamp_max() function
      return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(10, 3*49)

__output__  = m(x1)