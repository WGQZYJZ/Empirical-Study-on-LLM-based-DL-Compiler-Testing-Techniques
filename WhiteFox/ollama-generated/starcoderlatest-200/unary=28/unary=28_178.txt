
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, min_value=0, max_value=None):
        v1 = self.linear(x1)
        if max_value is None:
            max_value = 2 ** (torch.max(v1).item() + 1) - 1
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Keyword arguments for clamping min and max values
min_value = -5
max_value = 10
