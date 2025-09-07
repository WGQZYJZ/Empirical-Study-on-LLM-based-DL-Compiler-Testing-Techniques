
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(512, 512)
 
    def forward(self, x1):
        v1 = self.mm(x1)
        v2 = self.mm(v1)
        v3 = v1 + v2 
        return v3


# Initializing the model
m  = Model()


# Inputs to the model