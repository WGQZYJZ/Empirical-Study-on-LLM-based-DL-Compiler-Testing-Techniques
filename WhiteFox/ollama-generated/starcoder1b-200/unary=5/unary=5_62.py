
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x2):
        v2 = self.conv(x2) * 0.5
        v3 = v2 * 0.7071067811865476
        v4 = torch.erf(v3) + 1
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()


