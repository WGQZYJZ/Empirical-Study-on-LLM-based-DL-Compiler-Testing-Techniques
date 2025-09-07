

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 10)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()

# Inputs to the model with the keyword argument set to a constant 2
x1 = torch.randn(50, 10)
other_tensor  = torch.full((10,), fill_value=2.)
