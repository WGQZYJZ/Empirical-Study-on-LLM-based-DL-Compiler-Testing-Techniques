
class Model(torch.nn.Module):
    def __init__(self, d1: int = 64, d2: int = 64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, d1, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(d1, d2, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v1 * 0.5 + v2
        v4 = torch.erf(v3)
        v5 = v4  + 1
        v6 = v2  * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
