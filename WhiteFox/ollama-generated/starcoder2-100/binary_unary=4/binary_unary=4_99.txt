
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
 
        self.lin  = torch.nn.Linear(3 * 64 * 64, 10)
 
    def forward(self, x):
        v1  = self.lin(x)
        v2  = v1 + other
        v3  = F.relu(v2) # relu is imported from the torch.nn.functional module
        return v3


# Initializing the model
m  = Model(other)


# Inputs to the model