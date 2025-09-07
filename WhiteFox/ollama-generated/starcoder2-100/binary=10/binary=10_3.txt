
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + other # Here we use a tensor that is not "other" in the previous example to demonstrate the pattern
        return v2

# Initializing the model
m  = Model()

