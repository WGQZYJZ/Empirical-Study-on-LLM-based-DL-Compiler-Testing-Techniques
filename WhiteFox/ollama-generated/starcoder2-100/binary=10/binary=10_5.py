
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        v1 = self.lin(x)
        v2 = v1 + other
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
 x  = torch.randn(64, 32)
 __output__  = m(x)

