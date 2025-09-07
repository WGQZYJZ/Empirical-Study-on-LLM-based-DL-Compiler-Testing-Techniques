
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(1024, 5)
 
    def forward(self, x):
        v1 = self.lin(x)
        return v1


# Initializing the model
m = Model()

# Inputs to the model