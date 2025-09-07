
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3).clamp(min=0)
        v3 = torch.clamp(v2, max=6)
        v4 = v1 * v3
        return v4


# Initializing the model
m = Model()


