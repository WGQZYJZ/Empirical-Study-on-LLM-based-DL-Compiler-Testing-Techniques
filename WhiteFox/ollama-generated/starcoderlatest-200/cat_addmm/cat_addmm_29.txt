
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.addmm(x1, x2, x3)
        v2 = torch.cat([v1], dim)
        return v6
