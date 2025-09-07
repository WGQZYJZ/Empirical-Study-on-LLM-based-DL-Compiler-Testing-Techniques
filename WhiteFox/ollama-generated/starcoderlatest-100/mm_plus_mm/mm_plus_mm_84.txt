
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(3, 8)
        self.mm2 = torch.nn.Linear(7, 4)
 
    def forward(self, x1, x2):
        v1 = self.mm1(x1)
        v2 = self.mm2(x2)
        v3 = torch.mm(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 7, 64, 64)
