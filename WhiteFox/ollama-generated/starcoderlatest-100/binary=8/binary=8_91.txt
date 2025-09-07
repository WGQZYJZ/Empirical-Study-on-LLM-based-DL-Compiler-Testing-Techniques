
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other is None:
            return v1
        else:
            return v1 + other


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
