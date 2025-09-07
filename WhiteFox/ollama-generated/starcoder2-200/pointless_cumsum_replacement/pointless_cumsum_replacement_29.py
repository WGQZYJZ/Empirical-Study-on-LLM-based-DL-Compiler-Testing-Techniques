
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        return None


# Initializing the model
m  = Model()
 
  # Inputs to the model
x1 = torch.randn(87)
 
__output__  = m(x1)
