
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, -9570.46875)
        v3 = torch.clamp_max(v2, 2333.03125)
        return v3

# Initializing the model