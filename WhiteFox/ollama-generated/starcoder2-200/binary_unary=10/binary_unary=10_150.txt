
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1 = torch.nn.Linear(x1)
        v2  = v1 + other
        return torch.nn.ReLU()(v2)

# Initializing the model
m  = Model()

 # Inputs to the model
other = torch.randn(4, 5)
  x1 = torch.randn(3, 7800, 19600)
 
  __output__  = m(x1, other)
