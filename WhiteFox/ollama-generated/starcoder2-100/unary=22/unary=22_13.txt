
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(50, 1)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = torch.tanh(v1)
        return v2

# Initializing the model
m = Model()

