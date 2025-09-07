
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(1024, 358)
 
    def forward(self, x1, other):
        v1 = self.lin(x1)
        v2 = v1 + other 
        v3 = F.relu(v2)
        return v3


# Initializing the model with the `other` tensor as an input argument