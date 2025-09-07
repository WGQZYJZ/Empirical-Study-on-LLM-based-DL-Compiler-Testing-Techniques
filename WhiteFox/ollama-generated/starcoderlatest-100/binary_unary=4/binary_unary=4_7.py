
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.lin = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 + other if other is not None else None
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
