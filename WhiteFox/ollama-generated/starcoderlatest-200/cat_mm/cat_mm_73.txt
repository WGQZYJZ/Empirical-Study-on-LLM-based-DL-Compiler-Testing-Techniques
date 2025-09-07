
class Model(torch.nn.Module):
    def __init__(self, kernel_size: int = 3):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1] * len(v1), dim=0)
        return v2
