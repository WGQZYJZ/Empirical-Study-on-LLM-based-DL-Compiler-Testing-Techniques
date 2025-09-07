
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        return v3


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
