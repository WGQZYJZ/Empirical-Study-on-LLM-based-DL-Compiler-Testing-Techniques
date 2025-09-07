
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.nn.functional.full

    def forward(self, x1, x2=None):
        if x2 is None:
            return self.full((x1,), 1.0)
        else:
            return self.full((x1, x2), 1.0)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 64, 64)
