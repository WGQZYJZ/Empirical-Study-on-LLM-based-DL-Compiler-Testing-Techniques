
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()
other  = random_scalar() # random scalar that is not equal to 0 or 1

# Inputs to the model
x1  = torch.randn(3, 8)
