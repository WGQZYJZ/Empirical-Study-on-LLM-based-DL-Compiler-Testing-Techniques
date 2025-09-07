
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=0.)
        v3 = torch.clamp_max(v2, max_value=1.)
        return v3


# Initializing the model and providing keyword arguments for linear layer
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 64)
