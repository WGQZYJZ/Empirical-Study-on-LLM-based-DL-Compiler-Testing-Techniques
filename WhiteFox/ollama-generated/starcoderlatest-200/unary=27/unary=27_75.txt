
class Model(torch.nn.Module):
    def __init__(self, min_value: float=1e-2, max_value: float=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()
# You can change the keyword arguments to `m = Model(-0.5)` and `m = Model(min_value=-0.5)` to run the test successfully.

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
