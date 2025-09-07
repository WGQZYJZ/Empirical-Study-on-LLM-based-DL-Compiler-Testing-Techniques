
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(32, 32)
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x1)
        v2 = v1 + inp if (inp is not None) else v1
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4, 32, 64, 64)
