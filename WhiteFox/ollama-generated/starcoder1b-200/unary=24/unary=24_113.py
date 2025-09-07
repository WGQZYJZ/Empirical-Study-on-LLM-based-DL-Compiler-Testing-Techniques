
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1).view(-1)
        v2 = torch.where(v1 > 0, v1 * -0.5, v1 * 0.7071067811865476)
        v3 = torch.erf(v2) + 1
        v4 = (v2 * v3).view(-1)
        return v4


# Initializing the model
m = Model()
