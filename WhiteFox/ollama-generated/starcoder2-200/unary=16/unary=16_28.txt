
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(80, 1)
 
    def forward(self, x2):
        v3 = self.lin(x2)
        v4 = torch.relu(v3)
        return v4


# Initializing the model