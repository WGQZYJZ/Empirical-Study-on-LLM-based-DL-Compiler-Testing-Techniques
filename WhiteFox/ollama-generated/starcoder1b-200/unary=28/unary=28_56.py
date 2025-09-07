
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.5, max_value=1.5):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
        self.clamp_min = torch.nn.ClampMin(-max_value, min_value)
        self.clamp_max = torch.nn.ClampMax(-min_value, max_value)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.clamp_min(v1, min_value=min_value)
        v3 = self.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
