
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, dim):
        v1 = self.conv(x1)
        t1 = v1 @ m[m] + 0.5
        t2 = torch.cat([t1], dim)
        return t2
