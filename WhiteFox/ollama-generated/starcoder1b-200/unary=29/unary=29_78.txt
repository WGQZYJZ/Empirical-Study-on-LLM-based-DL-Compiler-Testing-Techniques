
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1, min_value=0.0, max_value=1.0):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__, __output__[0] = m(x1, min_value=-5.0, max_value=2.0)

