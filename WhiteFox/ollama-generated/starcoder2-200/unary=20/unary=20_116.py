
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.sigmoid(x1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
  x1 = torch.randn(4096, 576)
__output__  = m(x1)

