
class Model(torch.nn.Module):
    def __init__(self, min_value: float = -5.0, max_value: float = 5.0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 16, stride=16, padding=16)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
