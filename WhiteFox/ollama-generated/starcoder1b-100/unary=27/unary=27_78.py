
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-4, max_value=20.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = torch.clamp_min(self.conv(x1), self.min_value)
        v2 = torch.clamp_max(v1, self.max_value)
        return v2


# Initializing the model
m = Model()


