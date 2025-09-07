
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v = self.conv(x)
        return torch.where(v > 0, v * negative_slope, v)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 3, 64, 64)
