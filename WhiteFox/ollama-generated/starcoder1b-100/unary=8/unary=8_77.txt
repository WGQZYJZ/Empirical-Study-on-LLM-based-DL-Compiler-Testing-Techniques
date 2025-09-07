
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 4, 1, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = torch.clamp(v3, min=1, max=7)
        v5 = v1 * v4
        return v5


# Initializing the model
m = Model()


