
class Model(torch.nn.Module):
    def __init__(self, min_value: torch.Tensor = None, max_value: torch.Tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._min_value = min_value
        self._max_value = max_value
 
    def forward(self, x1: torch.Tensor):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=self._min_value)
        v3 = torch.clamp_max(v2, max_value=self._max_value)
        return v3


# Initializing the model
m = Model(min_value=torch.tensor([0.0]), max_value=torch.tensor([1.0]))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
