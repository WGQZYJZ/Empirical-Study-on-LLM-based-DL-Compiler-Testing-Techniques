
class Model(torch.nn.Module):
    def __init__(self, min=10., max=25.)
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x):
        v1  = linear(x)
        v2  = clamp_min(v1, min_value=minimum) 
        v3  = clamp_max(v2, max_value=maximum)
    return v3
 
# Initializing the model
m  = Model()

 # Inputs to the model
 x   = torch.randn(10000, 15498) 
 