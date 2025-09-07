
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 8)
        self.m2 = torch.nn.Linear(4, 8)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.m1(x1)
        v2 = self.m2(x2)
        v3 = torch.mm(v1, v2)
        v4 = torch.mm(v3, v1)
        v5 = torch.mm(v3, v4)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 4, 64, 64)
x3  = torch.randn(8, 3, 1, 1)
x4  = torch.randn(8, 4, 1, 1)
