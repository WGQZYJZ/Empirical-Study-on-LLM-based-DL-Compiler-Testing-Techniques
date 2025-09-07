
class Model(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()
 
    def forward(self, x1, y2):
        v3  = torch.cat([x1, y2])
        return v3

 # Initializing the model
m  = Model()
 
  # Inputs to the model
  v0 = torch.randn(4, 5)
  v1 = torch.randn(4, 6)
  