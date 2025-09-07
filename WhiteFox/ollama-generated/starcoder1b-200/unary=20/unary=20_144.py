
class Upsample(torch.nn.Module):
    def __init__(self, upsample=True):
        super().__init__()
        self.upsample = upsample

    def forward(self, x1):
        if self.upsample:
            return F.interpolate(x1, scale_factor=2, mode='nearest')
        else:
            return x1

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
        self.upsample = Upsample()

    def forward(self, x1):
        v1 = self.conv(x1)
        return self.upsample(v1)


# Initializing the model
m = Model()
