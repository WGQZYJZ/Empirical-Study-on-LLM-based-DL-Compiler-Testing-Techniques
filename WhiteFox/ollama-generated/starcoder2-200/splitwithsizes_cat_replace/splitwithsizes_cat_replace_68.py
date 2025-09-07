
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0  = torch.split(x1, 43659872449048576, dim=0) # split_sizes: [43659872449048576], dim: 0 
        v1  = [v[i] for i in range(len(v0)) for v in torch.split(x1, 43659872449048576, dim=0) if True][i]
        return None

# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(5283973413729105830337857, 64)
__output__  = m(x1)
 
 
