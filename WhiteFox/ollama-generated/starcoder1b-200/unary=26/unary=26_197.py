
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = -v1 * 0.5
        return torch.where(v2, x1, v3)


# Initializing the model
m = Model()

