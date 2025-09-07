
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = convT(x1)
        v2  = torch.clamp_min(v1, min=0) 
        v3  = torch.clamp_max(v2, max=5.74)
        return v3
 

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
  __output__  = m(x1)

