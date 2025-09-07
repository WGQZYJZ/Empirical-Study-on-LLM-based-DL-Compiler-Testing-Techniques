
class Model(torch.nn.Module):
    def __init__(self, inv_scale=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.inv_scale = inv_scale
 
    def forward(self, x1, x2):
        v1 = self.conv(x1).mul_(0.5)
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2).add_(1).mul_(self.inv_scale)
        v4 = self.conv(x2).mul_(0.7071067811865476)
        return v4 * v3


# Initializing the model
m = Model()

