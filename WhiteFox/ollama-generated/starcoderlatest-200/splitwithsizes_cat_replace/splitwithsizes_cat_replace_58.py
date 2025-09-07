
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.split(v1, [0.5], dim=0)[0]
        v3 = torch.cat([torch.split(v2, [0.7071067811865476], dim=0)[0]], dim=0)
        v4 = torch.erf(torch.split(v3, [1], dim=0)[0])
        return v4

