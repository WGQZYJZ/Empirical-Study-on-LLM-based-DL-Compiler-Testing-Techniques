
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(10, 5)
 
    def forward(self, x1, x2, inp):
        v1 = self.mm(x1)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()
inp = torch.randn(1, 5)
