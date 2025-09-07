
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3).clamp_(min=0)
        v3 = torch.clamp_max((v2 * 6.0), 6) / 6.0
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
