
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.clamp_min(v, min_value=min_value)
        v = torch.clamp_max(v, max_value=max_value)
        return v


# Initializing the model
m  = Model(0.5, 1.2)

# Inputs to the model
x1 = torch.randn(1, 10)
