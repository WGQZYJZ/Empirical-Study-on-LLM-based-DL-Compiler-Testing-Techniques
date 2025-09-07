
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v2  = self._linear(x1) + other
        return torch.relu(v2)

 # Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(30, 4) 
 __other__  = torch.randn(80)
 