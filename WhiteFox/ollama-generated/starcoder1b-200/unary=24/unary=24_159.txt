
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, 1 - v1, 0) * -1
        v3 = v1 * -0.7071067811865476
        v4 = torch.abs(v2).add_(torch.sign(v1))
        return v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
