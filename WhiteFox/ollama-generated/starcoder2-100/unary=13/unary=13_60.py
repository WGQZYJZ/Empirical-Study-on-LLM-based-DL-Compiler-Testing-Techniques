
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32 * 32, 10)
 
    def forward(self, x):
        v1 = self.lin(x)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(64, 3, 32, 32)
