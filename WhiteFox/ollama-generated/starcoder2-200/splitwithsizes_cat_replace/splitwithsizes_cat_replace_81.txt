
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.split(x1, [256], 0) + [None]
 
 # Initializing the model
 m = Model()
 
# Inputs to the model
 x1  = torch.randn(384, 3, 3, 3)
  __output__  = m(x1)
