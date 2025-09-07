
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=True)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2 = other_tensor - v1 
        v3 = F.relu(v2) 
        return v3


# Initializing the model
m2 = Model2()
 
 # Inputs to the model
  x1 = torch.randn(8, 3)
  other_tensor = torch.randn(8).sum()
  
__output__  = m2(x1)
