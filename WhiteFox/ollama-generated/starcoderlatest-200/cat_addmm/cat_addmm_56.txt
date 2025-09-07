
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, v1.transpose(-2, -1), 0)
        v2 = torch.cat([v2], dim=-3)
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
