
class Model(torch.nn.Module):
    def __init__(self, min_value=-1000, max_value=1000):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m = Model(min_value=-5, max_value=5)

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
