
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.tconv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return self.tconv(v5)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
