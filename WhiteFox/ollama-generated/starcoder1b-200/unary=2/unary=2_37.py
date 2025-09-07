
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.ct   = torch.nn.ConvTranspose2d(8, 3, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        c1 = self.ct(v1) * 0.5
        v2 = c1 * v1 * v1 * v1
        c2 = torch.erf(v2) + 1
        v3 = c2 * (c1  + 1)
        return self.ct(v3)


# Initializing the model
m = Model()


