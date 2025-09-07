
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.linear2 = torch.nn.Linear(64, 32)
 
    def forward(self, x1, inp):
        v1 = self.linear1(x1) * 0.5 + inp
        v2 = self.linear2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 32, 64, 64)
inp = torch.rand(4, 32, 64, 64)
