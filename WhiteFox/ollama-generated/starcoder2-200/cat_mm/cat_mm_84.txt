
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(2, 3)
 
    def forward(self, x1, x2):
        v0 = self.mm(x1)
        v1 = self.mm(x2)
        v2 = torch.cat([v0, v1])
        return v2


# Initializing the model
m  = Model()


 # Inputs to the model