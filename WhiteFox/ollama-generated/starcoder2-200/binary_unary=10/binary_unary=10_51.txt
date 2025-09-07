
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1  = torch.nn.Linear(507268, 3)
        self.lin2  = torch.nn.Linear(4997, 1)
 
    def forward(self, x1):
        v1  = self.lin1(x1) 
        v2  = v1 + other_tensor
        v3  = torch.nn.functional.relu(v2)  
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
other_tensor  = torch.randn(507, 4998)
input_tensor  = torch.ones([1] + list(other_tensor.size()))
  __output__   = m(x1)

