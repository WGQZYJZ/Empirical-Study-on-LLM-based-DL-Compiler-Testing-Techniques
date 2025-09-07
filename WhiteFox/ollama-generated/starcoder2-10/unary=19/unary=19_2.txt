
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32768, 2)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.sigmoid(v1) # sigmoid
        return v2


# Initializing the model
m = Model()
 
