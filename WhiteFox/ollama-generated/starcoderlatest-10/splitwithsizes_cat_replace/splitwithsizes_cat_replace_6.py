
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1_a = torch.split(x1, [1, -1], dim=1)[0]
        v1_b = torch.split(x1, [-1, 1], dim=2)[0]
        v2 = torch.cat([v1_a, v1_b], dim=1)
        return v2
