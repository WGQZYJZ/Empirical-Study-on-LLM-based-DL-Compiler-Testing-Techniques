
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).mul_(0.7071067811865476).add_(1)
        v3 = v2.mul_(0.7071067811865476).mul_(0.5)
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (v2 * v5).mul_(0.5)
        return v6


# Initializing the model
m = Model()

x1 = torch.randn(1, 3, 64, 64)
