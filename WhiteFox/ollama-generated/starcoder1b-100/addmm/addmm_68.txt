
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(16, 3)
 
    def forward(self, x1, inp=None):
        y1 = self.m(x1) + inp
        return y1


# Initializing the model
m = Model()


