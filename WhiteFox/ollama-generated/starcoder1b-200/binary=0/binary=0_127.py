
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + self.other


# Initializing the model
m = Model()
m.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
m.other = torch.randn(1, 3, 64, 64)
