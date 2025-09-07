
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        k = torch.randn(4, 3, 64, 64)
        v = torch.randn(4, 8, 64, 64)
        q = torch.randn(4, 3, 50, 50)
        