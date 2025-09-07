
class Model(torch.nn.Module):
    def __init__(self, min_value=-1, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, min_value=None, max_value=None):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).clamp(min_value=min_value)
        v3 = (v1 * 0.7071067811865476).clamp(max_value=max_value)
        return v2


# Initializing the model
m = Model()


