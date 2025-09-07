
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.m2 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = self.m1(x1) * inp
        v2 = self.m2(v1) + inp
        return v2


# Initializing the model
m = Model()


# Inputs to the model
inp  = torch.randn(1, 3, 64, 64)
x1   = torch.randn(1, 3, 64, 64)
