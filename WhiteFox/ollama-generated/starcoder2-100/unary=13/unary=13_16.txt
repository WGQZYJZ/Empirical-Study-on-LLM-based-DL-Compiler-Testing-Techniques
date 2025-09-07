
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32*10, 6)
 
    def forward(self, x1):
        v1  = self.lin(x1) 
        v2  = torch.sigmoid(v1) 
        return v1 * v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(3, 32*10)

__output__  = m(x1).mean().item()

