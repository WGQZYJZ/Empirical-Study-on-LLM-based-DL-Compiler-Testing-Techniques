
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-4, max_value=None):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        if max_value is not None:
            v2 = torch.clamp_min(v1, min_value=0)
            v3 = torch.clamp_max(v2, max_value=max_value)
        else:
            v3 = torch.clamp_min(v1, min_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
