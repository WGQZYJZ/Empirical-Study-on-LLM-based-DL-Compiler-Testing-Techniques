
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1[:, :64] * 0.5 + v1[:, 9223372036854775807:]
        v3 = torch.cat([v1, x2], dim=1)
        return v3


# Initializing the model
m = Model()


