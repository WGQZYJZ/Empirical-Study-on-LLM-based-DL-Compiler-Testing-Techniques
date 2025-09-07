
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5


# Input for the model and expected output
x1 = torch.randn(1, 3, 64, 64)
__expected_output__ = x1 * 0.28125 + 3 * torch.clamp_min(x1 * 0.78125 + 3, 0) / 6


