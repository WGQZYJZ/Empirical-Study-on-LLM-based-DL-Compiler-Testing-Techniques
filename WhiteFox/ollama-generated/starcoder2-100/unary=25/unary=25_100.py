
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 > 0
        v3  = v1 * -2.95747469
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3)
 
 __output__  = m(x1)