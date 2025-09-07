
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(20, 8)
 
    def forward(self, x1):
        v1 = self.lin1(x1)
        v2 = torch.clamp(v1 + 3, min=0, max=6)
        v4 = v2 / 6
        return v4


# Initializing the model
m = Model()
 

# Inputs to the model