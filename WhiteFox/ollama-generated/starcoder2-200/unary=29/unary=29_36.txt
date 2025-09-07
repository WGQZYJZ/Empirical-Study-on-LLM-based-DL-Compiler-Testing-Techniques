
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.clamp_min(x1)
        v2  = torch.clamp_max(v1, 4096)
        return v2

 # Initializing the model
m = Model()
 
 ## Inputs to the model
x1 = torch.rand(1, 3, 64, 64) 
 __output__  = m(x1)
