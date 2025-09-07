
class Model(torch.nn.Module):
    def __init__(self, max_value=50., min_value=-10.):
        super().__init__()
 
    def forward(self, x):
        v1  = torch.nn.Linear(x, y)(x)
        v2  = torch.clamp(v1, max_value)
        return torch.clamp(v2, -min_)

# Initializing the model
m  = Model()

 # Inputs to the model 
 x = torch.randn(30, 45, 76)
 __output__= m (x)
 
 