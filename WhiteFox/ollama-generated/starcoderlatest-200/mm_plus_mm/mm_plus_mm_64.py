
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(24, 8)
        self.m2 = torch.nn.Linear(64, 8)
 
    def forward(self, x1):
        v1 = self.m1(x1)
        v2 = self.m2(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 24, 608, 32)
x2 = torch.randn(4, 64, 608, 32)
