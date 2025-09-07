
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0, max_value=255):
        v1 = self.conv(x1)
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = torch.clamp_min(v3, min_value)
        v5 = torch.clamp_max(v4, max_value)
        return v5


# Initializing the model
m = Model()


