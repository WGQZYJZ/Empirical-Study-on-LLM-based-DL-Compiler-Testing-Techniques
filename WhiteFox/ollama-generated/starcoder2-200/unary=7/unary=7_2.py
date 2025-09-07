
class Model(torch.nn.Module):
    def __init__(self, l1, l2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * clamp(min=0, max=6, l1 + 3)
        v3 = v2 / 6
