
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1, min_value, max_value)
        return v2


# Initializing the model with keyword arguments
m = Model(min_value=0., max_value=1.)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
