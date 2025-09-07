
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model2()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
