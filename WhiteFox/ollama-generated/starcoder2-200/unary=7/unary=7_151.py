
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.lin1 = torch.nn.Linear(4096, 2578)
        self.lin2 = torch.nn.Linear(2578, 3)
 
    def forward(self, x):
        v = self.lin1(x)
        v = self.lin2(v + 3) / 6
        return v

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(1000, 4096)
 
__output__  = m(x)
