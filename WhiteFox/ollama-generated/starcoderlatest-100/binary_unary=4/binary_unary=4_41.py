
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other == None:
            other = torch.randn(1, 8)
        self.lin = torch.nn.Linear(3, 8)
        self.other = other
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 + self.other
        v3 = torch.relu(v2)
        return v3


# Initializing the model with a parameter other
m = Model(other=torch.randn(1, 8))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
