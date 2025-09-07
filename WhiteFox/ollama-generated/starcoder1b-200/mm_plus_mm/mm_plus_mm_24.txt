
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(3, 8)
        self.m2 = torch.nn.Linear(3, 8)
 
    def forward(self, x1, x2):
        v1 = self.m1(x1)
        v2 = self.m2(x2)
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3)
x2  = torch.randn(1, 8)
