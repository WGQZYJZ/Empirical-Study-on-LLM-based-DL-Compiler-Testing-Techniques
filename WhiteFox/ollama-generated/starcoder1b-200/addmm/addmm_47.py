
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(50, 3)
 
    def forward(self, x1, inp=2):
        v1 = torch.mm(x1, x2) + inp
        return v1


# Initializing the model
m = Model()
inp = torch.randn(50)
