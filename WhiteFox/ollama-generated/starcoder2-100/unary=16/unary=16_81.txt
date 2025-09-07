
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64*64*3, 1)
 
    def forward(self, x2):
        v1  = self.linear(x2)
        v2  = nn.functional.relu(v1)
        return v2

 # Initializing the model
m = Model()
 
 # Inputs to the model
  x1  = torch.randn(1, 3, 64, 64) 
  x2  = torch.flatten(x1, start_dim=1)
__output__  = m(x2)

