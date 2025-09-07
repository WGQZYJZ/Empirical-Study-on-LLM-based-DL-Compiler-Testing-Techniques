
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 4, 5)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=0)
        v2 = v1.view(-1, 64, 8, 8)
        