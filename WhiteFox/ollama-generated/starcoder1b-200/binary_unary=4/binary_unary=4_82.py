
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other   = other
 
    def forward(self, x1, other=None):
        if other is None:
            return self.linear(x1)
        else:
            return self.linear(x1) + other


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
