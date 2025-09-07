
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other):
        v2 = self.linear(x1) + other
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
v1 = torch.randn(1, 3)
other_tensor  = torch.randn(1, 8)
  __output__  = m(v1, other_tensor)
  
