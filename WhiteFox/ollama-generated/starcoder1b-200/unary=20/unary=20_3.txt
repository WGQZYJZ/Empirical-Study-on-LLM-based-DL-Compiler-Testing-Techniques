
class Upsample(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        return v2


# Initializing the model
u = Upsample()

 # Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
