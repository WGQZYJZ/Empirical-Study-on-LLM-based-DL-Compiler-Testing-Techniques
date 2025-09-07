
class Model(torch.nn.Module):
    def __init__(self, maxval = 1000., minval=-564839):
        super().__init__()
        self.lin  = torch.nn.Linear(70, 1)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.clamp_min(v1, minval=(-564839)) # the minimum value is provided as a keyword argument 
        v3  = torch.clamp_max(v2, maxval=1000.) # the maximum value is provided as a keyword argument 
        return v3

# Initializing model with keyword arguments
m  = Model(maxval=-564839)

