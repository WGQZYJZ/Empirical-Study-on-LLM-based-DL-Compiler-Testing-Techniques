
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(5, 10)
 
    def forward(self, x1, other):
        v1  = self.lin(x1) + other 
        return v1

# Initializing the model
m = Model()

