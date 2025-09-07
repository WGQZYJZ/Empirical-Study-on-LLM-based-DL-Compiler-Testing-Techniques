
class Model(torch.nn.Module):
    def __init__(self, min=0., max=1.)
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x1) 
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, 0.)
        v3  = torch.clamp_max(v2, 1.)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(4)
__output__  = m(x1)