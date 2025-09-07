
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(20, 5)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 - other
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
other  = torch.randn(3, 40).abs() / (torch.std(other, dim=0) + 1e-5)
x1  = torch.randn(3, 20)
__output__  = m(x1)

