
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v2 = self.conv(x2) + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v2 * v4
        return v5 / 6


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
