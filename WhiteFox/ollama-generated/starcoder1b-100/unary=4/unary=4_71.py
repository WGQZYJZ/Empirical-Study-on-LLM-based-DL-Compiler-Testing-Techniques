
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v = self.linear(x)
        v = v * 0.5
        v = v * 0.7071067811865476
        v = torch.erf(v)
        v = v + 1
        v = v * v
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3)
