
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1, other=None):
        if other is not None:
            v1 = self.linear(x1 + other)
        else:
            v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 32, 64, 64)
