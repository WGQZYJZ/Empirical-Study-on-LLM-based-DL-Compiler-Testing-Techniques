
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=32.0):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)
        self.clamp_min  = torch.nn.functional.clamp_min
        self.clamp_max  = torch.nn.functional.clamp_max
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = self.clamp_min(v1, min_value=min_value)
        v3 = self.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m = Model(min_value=-5.0, max_value=5.0)


