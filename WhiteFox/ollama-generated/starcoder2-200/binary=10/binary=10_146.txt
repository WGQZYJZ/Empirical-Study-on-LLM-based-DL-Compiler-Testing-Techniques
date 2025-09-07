
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(4,1)
 
    def forward(self, x1):
        v1  = self.lin(x1) 
        return v1


# Initializing the model