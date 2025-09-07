
class Model(torch.nn.Module):
    def __init__(self, min_value=-100., max_value=100.):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model with minimum and maximum values of -100 and 100 respectively.
m = Model(-100., 100.)

# Inputs to the model
x1 = torch.randn(1, 32, 56, 56)
