
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 2)
 
    def forward(self, x0=None, x1=None, inp=None):
        v1 = torch.mm(x0, x1) + inp
        return v1


# Initializing the model
m = Model()

# Inputs to the model