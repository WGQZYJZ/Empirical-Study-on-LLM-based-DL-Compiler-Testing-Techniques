
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, -0.9564789395414505)
        v3 = torch.clamp_max(v2, 0.4900522820070577)
        return v3

# Initializing the model
m = Model()

