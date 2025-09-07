
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(3, 50)
        self.lin2 = torch.nn.Linear(50, 70)
 
    def forward(self, x1):
        v1  = self.lin1(x1)
        v2  = v1 - other 
        v3  = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model, with a different number of elements in each dimension
x1 = torch.randn(500, 3).to('cuda')
 
__output__   = m(x1).data