
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(32, 4)
 
    def forward(self, x1, inp=None):
        v1 = self.m(x1) + inp
        return v1


# Initializing the model
m = Model()

