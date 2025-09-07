
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(100, 3)
        self.other   = other
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        return v1 + self.other(**kwargs)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
