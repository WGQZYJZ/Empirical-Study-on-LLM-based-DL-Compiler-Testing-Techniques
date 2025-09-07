
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-3, max_value=1 - 1e-3):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
        self._min_value = min_value
        self._max_value = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=self._min_value)
        v3 = torch.clamp_max(v2, max=self._max_value)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64 * 64)
