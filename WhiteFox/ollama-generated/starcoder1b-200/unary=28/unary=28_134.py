
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=5):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.clamp_min  = lambda t: torch.clamp_min(t, min_value)
        self.clamp_max  = lambda t: torch.clamp_max(t, max_value)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.clamp_min(v1)
        v3 = self.clamp_max(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3)
