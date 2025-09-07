
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        return v1


# Initializing the model
m = Model(torch.randn(1, 32))


# Inputs to the model
x1 = torch.randn(1, 8)
