
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(784, 100)
 
    def forward(self, x):
         v1 = self.lin(x)
         v2 = v1 * clamp(min=0, max=6, v1 + 3) 
         v3 = v2 / 6 
         return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x = torch.randn(1, 784)
 
# Outputs from the model 
__output__  = m(x).view(-1)

