
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1, min=min_value, max=max_value)
        return v2


# Initializing the model
m = Model(0.0, 0.75)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
