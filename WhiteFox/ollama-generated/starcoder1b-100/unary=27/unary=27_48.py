
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value, max_value):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 + torch.clamp_min(v1, min_value)
        v3 = v1 * 0.7071067811865476 + torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()


