
class Model(torch.nn.Module):
    def __init__(self, min_value=0.0, max_value=1.0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Initializing the model
m = Model()


