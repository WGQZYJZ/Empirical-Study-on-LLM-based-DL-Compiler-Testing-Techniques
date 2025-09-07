
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        query  = torch.randn(2, 2, 4, 5)
        key    = torch.randn(2, 2, 4, 5)
        value  = torch.randn(1, 2, 3, 4)
        