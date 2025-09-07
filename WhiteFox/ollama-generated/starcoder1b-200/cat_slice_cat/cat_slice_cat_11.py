
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1[:, :, size // 2: size - (size // 2)]
        v3 = torch.cat([v1, v2], dim=-1)
        return v3


# Initializing the model
m = Model()


