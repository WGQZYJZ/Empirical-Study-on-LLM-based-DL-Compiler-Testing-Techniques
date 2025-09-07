
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 64)
        self.m2 = torch.nn.Linear(64, 8)
 
    def forward(self, x1, x2, x3, x4):
        t1 = torch.mm(x1, x2)
        t2 = torch.mm(x3, x4)
        t3 = t1 + t2
        return t3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 64, 64, 64)
x3 = torch.randn(1, 3, 64, 64)
x4 = torch.randn(1, 8, 64, 64)
