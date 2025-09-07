
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        m1 = v1 > 0
        v2 = v1 * negative_slope
        m2 = torch.where(m1, v1, v2)
        return m2


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
