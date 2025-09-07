
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 64)
        self.m2 = torch.nn.Linear(8, 3)
 
    def forward(self, x1, x2=None):
        inp = torch.randn(1, 64, 64, 3)
        t1 = self.m1(x1)
        t2 = t1 + inp
        return self.m2(t2)


# Inputs to the model
x1 = torch.randn(1, 64, 64, 8)
x2 = torch.randn(1, 3, 64, 64)
