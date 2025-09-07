
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(80*32, 45)
        self.activation = torch.nn.Sigmoid()
 
    def forward(self, x1): 
        v1 = self.linear(x1)        
        v2 = self.activation(v1)
        v3 = v1 * v2 
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(80, 32)
__output__= m(x1)

Model: You are a source code analyzer for PyTorch.

User: 