
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_)
        v3  = torch.clamp_max(v2, max_)
        return v3

# Initializing the model
m  = Model(4.,5.)

 # Inputs to the model
x1  = torch.randn(7, 8)
__output__  = m(x1)

