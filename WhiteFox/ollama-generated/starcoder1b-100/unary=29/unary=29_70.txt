
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-7, max_value=1 - 1e-7):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, min_value=None, max_value=None):
        if min_value is not None:
            v1 = self.conv(x1).clamp(min_value)
        else:
            v1 = self.conv(x1)
        if max_value is not None:
            v2 = torch.clamp_max(v1, max_value)
        else:
            v2 = torch.clamp_max(v1, min_value=min_value)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
