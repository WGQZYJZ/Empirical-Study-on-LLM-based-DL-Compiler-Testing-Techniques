
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        l2 = self.linear(v1) + 3
        return torch.clamp_min(l2, 0), torch.clamp_max(l2, 6) / 6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__, __gradient__ = m(x1)


