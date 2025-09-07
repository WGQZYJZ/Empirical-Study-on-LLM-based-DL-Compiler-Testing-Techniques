
class Model(torch.nn.Module):
    def __init__(self, min_value=-100, max_value=100):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, min_value=None, max_value=None):
        if min_value is None:
            min_value = 0
        if max_value is None:
            max_value = 256

        v1 = self.conv(x1)
        v2 = torch.clamp(v1 * 0.5, min=min_value)
        v3 = torch.clamp(v2 * 0.7071067811865476, max=max_value)

        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
