
class Model(torch.nn.Module):
    def __init__(self, min=0., max=1.):
        super().__init__()
        self.linear = torch.nn.Linear(48, 3)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, min)
        v3 = torch.clamp_max(v2, max)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
__inputs__ = torch.randn(10, 48)
__output__  = m(__inputs__)
 
