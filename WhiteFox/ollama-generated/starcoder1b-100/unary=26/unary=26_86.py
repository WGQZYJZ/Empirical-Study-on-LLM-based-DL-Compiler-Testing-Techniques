
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * negative_slope
        v3 = torch.where(v1, x1, v2)
        return v3


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
