
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value=None):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        if not hasattr(self, "min_value") or self.max_value is None:
            self.min_value = min(x1)
            self.max_value = max(x1)
        return torch.clamp_min(v1, self.min_value), torch.clamp_max(v1, self.max_value)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
