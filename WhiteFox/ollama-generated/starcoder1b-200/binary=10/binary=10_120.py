
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
        self.other   = other
 
    def forward(self, x):
        v1 = self.linear(x) + self.other
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
