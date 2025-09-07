
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 4)
 
    def forward(self, x1, other=None):
        v1 = self.lin(x1) + (other or x1) * x1
        return F.relu(v1)


# Initializing the model
m  = Model()
 

# Inputs to the model
x1  = torch.randn(1, 3)
