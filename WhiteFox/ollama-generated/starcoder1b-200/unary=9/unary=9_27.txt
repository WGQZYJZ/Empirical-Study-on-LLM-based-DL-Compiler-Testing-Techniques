
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1 + 3, 0)
        v3 = torch.clamp_max(torch.clamp(v2 / 6, 0, 6), 0, 6)
        return v3


# Initializing the model
m = Model()


