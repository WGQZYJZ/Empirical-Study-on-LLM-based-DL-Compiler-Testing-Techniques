
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1  *  0.7071067811865476
        v3  = torch.erf(v2)
        v4  = v3  + 1 
        v5  = v1  * v4    
        return v5

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(600, 1024)
