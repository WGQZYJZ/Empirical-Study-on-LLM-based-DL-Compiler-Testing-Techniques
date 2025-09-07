
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v2 ** 2
        v4 = torch.sqrt(v3)
        v5 = v4 * 2
        v6 = v5  + 1
        return v6


# Initializing the model
m = Model()


