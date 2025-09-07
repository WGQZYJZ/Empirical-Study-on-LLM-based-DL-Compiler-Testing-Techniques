
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = list(range(5))
        v4 = torch.cat([v1] * len(v2), dim=0)

        return v4
