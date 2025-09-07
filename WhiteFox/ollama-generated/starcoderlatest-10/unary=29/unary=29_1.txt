
class Model(torch.nn.Module):
    def __init__(self, max_value=10., min_value=-10.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 5, stride=2, padding=4)
        self._max_value = max_value
        self._min_value = min_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=self._min_value)
        v3 = torch.clamp_max(v2, max_value=self._max_value)
        return v3

# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
