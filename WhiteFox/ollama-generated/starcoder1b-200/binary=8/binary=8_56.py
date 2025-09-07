
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return self.conv(v1 + other)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other  = torch.randn(1, 8, 128, 128)
