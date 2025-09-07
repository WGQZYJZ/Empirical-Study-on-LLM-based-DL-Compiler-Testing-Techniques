
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 8)
        self.m2 = torch.nn.Linear(3, 4)

    def forward(self, x1):
        t1 = self.m1(x1)
        t2 = torch.cat([t1, t1, ..., t1], dim=0)
        return self.m2(t2)

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
