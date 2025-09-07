
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 1 / 4)
        v4 = torch.pow(v3, 2)
        v5 = torch.sqrt(v4 + 1)
        v6 = v5 * v2
        return v6


# Initializing the model
m = Model()


