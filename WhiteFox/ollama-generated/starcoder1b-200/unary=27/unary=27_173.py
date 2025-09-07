
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=255):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 0.5 * min_value
        v3 = v1 + 0.7071067811865476 * max_value
        return torch.clamp(v2 * v3, min=min_value, max=max_value)


# Initializing the model
m = Model()
