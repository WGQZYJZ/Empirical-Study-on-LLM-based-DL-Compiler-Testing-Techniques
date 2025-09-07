
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.split(x1, [40], dim=3)
        v6  = torch.cat([v2[i] for i in range(len(v2))], dim=3)
 
        return v6

 # Initializing the model
m  = Model()
 
 # Input to the model
 x1 = torch.randn(40,80,95, 95)
  __output__  = m(x1)

