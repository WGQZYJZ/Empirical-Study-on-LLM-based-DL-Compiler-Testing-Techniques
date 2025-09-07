
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = (v1 + 1).log()
        negative_slope = -0.2
        v3 = v2 * negative_slope
        return torch.where(v2 > 0, v1, v3)


# Initializing the model
m = Model()

