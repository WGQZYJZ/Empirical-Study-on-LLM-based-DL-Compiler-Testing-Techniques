
class Model(torch.nn.Module):
    def __init__(self, other=10):
        super().__init__()
        self.linear  = torch.nn.Linear(64, 32)
        self.other   = other
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64, 64)
