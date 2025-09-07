
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(5, 10)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
other  = torch.randn(5, 10)
x1 = torch.randn(8, 5)
__output__  = m(x1)
