
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        v1  = self.lin(x)
        return torch.tanh(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 32)
