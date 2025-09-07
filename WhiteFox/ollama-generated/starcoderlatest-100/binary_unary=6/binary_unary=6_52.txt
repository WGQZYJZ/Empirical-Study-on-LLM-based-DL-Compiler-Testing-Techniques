
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 - 0.5
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
