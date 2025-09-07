
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32*64*64, 10)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64).view(-1, 3*64*64)
