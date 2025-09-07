
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.m2 = torch.nn.Linear(400, 100)
        self.m3 = torch.nn.Linear(50, 70)
 
    def forward(self, x1):
        v1 = self.m1(x1)
        t1 = self.m2(v1) + inp
        v2 = self.m3(t1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
inp  = torch.randn(1, 3, 64, 64)
