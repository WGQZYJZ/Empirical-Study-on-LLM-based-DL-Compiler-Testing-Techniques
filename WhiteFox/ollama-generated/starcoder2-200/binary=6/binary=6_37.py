
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(4,8)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 - other

# Initializing the model
m = Model()


# Inputs to the model
other  = 0.5
x1 = torch.randn(16, 4)
