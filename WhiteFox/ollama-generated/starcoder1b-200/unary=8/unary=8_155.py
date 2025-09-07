
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v1 = self.conv(x2) + 3
        v2 = torch.clamp(v1, min=0)
        v3 = torch.clamp(v2, max=6)
        v4 = v1 * v3
        v5 = v4 / 6
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(8, 3, 64, 64)
