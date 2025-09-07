
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1)
        v2 = torch.cat([v1], dim)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(320, 512, 56, 56)
  