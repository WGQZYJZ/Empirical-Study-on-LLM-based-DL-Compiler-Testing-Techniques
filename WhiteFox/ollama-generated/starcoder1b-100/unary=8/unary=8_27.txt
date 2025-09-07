
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x2):
        v2 = self.conv(x2)
        v3 = v2 + 3
        v4 = torch.clamp(v3, min=0)
        v5 = torch.clamp(v4, max=6)
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
