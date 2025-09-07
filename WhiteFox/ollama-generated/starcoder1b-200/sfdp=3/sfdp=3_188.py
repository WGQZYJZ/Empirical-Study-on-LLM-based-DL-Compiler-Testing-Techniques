
class Model(torch.nn.Module):
    def __init__(self, scale_factor=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = scale_factor
 
    def forward(self, x1, k1):
        v1 = self.conv(x1)
        v2 = v1 * self.scale_factor
        return v2


# Inputs to the model
k1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1, k1)


