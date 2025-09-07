
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.split(v1, [4, 5], dim=1)
        # ...
        return v6


# Inputs to the model
x1 = torch.randn(3, 3, 28, 28)
