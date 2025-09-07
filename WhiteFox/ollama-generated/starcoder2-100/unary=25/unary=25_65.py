
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 1)

    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = (v1 > 0).float() * (-negative_slope) + (v1 <= 0).float() * v1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32)

# Calculating output for model with inputs x1
