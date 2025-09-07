
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.linear  = torch.nn.Linear(32*64*64, 8)
 
    def forward(self, x1): 
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_)
        v3  = torch.clamp_max(v2, max_) 
        return v3

# Initializing the model
m  = Model(0., -1.)

 # Inputs to the model
x1  = torch.randn(8, 32, 64, 64)
  __output__  = m(x1)