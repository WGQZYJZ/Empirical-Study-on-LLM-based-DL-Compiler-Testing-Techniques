
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.clamp = torch.nn.Clamp(min_value, max_value)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.clamp(v1)
        return v2

# Inputs to the model
min_value = -3000
max_value = 3000
