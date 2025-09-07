
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v2, 3)
        v4 = torch.exp(-v2)
        v5 = (v2 - v3 + v3 * v2) / v4
        return v9


# Initializing the model
m = Model()


