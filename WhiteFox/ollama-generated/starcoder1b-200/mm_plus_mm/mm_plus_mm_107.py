
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 4)
        self.m2 = torch.nn.Linear(4, 5)
 
    def forward(self, x1):
        v1 = self.m1(x1)
        v2 = self.m2(v1)
        return v2


# Inputs to the model
x1  = torch.randn(1, 3)
x2  = torch.randn(1, 4)
__output__  = m(x1) + m(x2)


