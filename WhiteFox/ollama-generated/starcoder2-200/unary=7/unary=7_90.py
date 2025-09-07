
class Model(torch.nn.Module):
    def __init__(self, n1=0):
        super().__init__()
        self.lin = torch.nn.Linear(32*32, 8 * 4 + 1)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1  * clamp(min=0, max=6, l1  + 3) 
        v3 = v2 / 6
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(4, 3*32*32) 
 