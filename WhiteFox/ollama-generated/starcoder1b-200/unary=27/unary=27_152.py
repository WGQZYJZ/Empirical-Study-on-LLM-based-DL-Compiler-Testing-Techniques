
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.9241356595787174):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5 + min_value
        v3 = v1 * 0.7071067811865476 + min_value
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


