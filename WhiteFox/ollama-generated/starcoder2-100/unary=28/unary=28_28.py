
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v0 =  torch.clamp_min(x1, min_value) 
        v1 =  torch.clamp_max(v0, max_value) 
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
input__  = [torch.randn(3), torch.randn(2)]
min_value  = input__[0]
max_value  = input__[1]
  