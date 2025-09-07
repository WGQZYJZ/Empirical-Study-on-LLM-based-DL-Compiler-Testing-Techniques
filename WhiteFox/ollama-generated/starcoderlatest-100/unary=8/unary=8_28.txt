
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(1024, 3, 8, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = torch.clamp(v1, min=0)
        v3 = torch.clamp(v2, max=6)
        v4 = v1 * v3
        v5 = v4 / 6
        return v5


# Initializing the model
m = Model()
x1 = torch.randn(1, 1024, 1, 1) # shape=(1, 1024, 1, 1)
