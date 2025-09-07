
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m = torch.nn.Linear(3, 8)
 
    def forward(self, x1, inp):
        v1 = self.m(x1) + inp
        return v1


# Inputs to the model
x1 = torch.randn(1, 3)
inp = torch.randn(1, 8)
