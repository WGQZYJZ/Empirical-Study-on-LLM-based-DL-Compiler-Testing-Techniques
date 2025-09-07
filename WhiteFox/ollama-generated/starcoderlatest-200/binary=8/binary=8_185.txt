
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is not None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if v is not None:
            