
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        v = self.conv(x)
        m = torch.where(v > 0., v, -self.negative_slope * v)
        return m


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
